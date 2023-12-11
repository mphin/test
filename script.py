import os
import re
import shutil
import requests

def download_file(url, dest_folder, dest_filename):
    response = requests.get(url, stream=True)
    file_path = os.path.join(dest_folder, dest_filename)
    with open(file_path, 'wb', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
    del response

def read_conf_file(file_path):
    conf_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#!"):
                key, value = re.match(r'#!(\w+)\s*=\s*(.*)', line).groups()
                conf_data[key] = value.strip()
    return conf_data

def generate_plugin_file(conf_file, script_folder, plugin_folder):
    name = conf_file.get('name') or read_script_info(script_folder, '项目名称')
    desc = conf_file.get('desc') or read_script_info(script_folder, '使用声明')
    open_url = conf_file.get('openUrl') or read_script_info(script_folder, '下载地址')
    author = conf_file.get('author') or read_script_info(script_folder, '脚本作者')
    homepage = conf_file.get('homepage') or read_script_info(script_folder, '电报频道')
    icon = conf_file.get('icon') or ''
    date = conf_file.get('date') or read_script_info(script_folder, '更新日期')
    mitm = conf_file.get('MITM') or read_script_info(script_folder, '[MITM]')
    script = conf_file.get('Script') or read_script_info(script_folder, '[rewrite_local]')

    plugin_content = f'''#!name = {name}
#!desc = {desc}
#!openUrl = {open_url}
#!author = {author}
#!homepage = {homepage}
#!icon = {icon}
#!date = {date}

[MITM]
{mitm}

[Script]
{script}
'''

    plugin_filename = os.path.splitext(os.path.basename(conf_file['path']))[0] + '.plugin'
    plugin_path = os.path.join(plugin_folder, plugin_filename)

    with open(plugin_path, 'w', encoding='utf-8') as plugin_file:
        plugin_file.write(plugin_content)

def read_script_info(script_folder, keyword):
    script_info_file = os.path.join(script_folder, 'info.txt')
    if os.path.exists(script_info_file):
        with open(script_info_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if keyword in line:
                    return line.split(':', 1)[1].strip()
    return ''

def main():
    tmp_folder = 'tmp'
    script_folder = 'Script'
    plugin_folder = 'plugin'

    if not os.path.exists(script_folder):
        os.makedirs(script_folder)
    if not os.path.exists(plugin_folder):
        os.makedirs(plugin_folder)

    for conf_filename in os.listdir(tmp_folder):
        if conf_filename.endswith('.conf'):
            conf_filepath = os.path.join(tmp_folder, conf_filename)
            conf_data = read_conf_file(conf_filepath)
            conf_data['path'] = conf_filepath  # 保存文件路径供后续使用
            download_url = conf_data.get('url')
            if download_url:
                download_file(download_url, script_folder, os.path.splitext(conf_filename)[0] + '.js')
                generate_plugin_file(conf_data, script_folder, plugin_folder)

if __name__ == "__main__":
    main()
