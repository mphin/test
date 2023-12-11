import os
import re
import shutil
import requests

def download_file(url, dest_folder, dest_filename):
    response = requests.get(url, stream=True)
    file_path = os.path.join(dest_folder, dest_filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)
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
    name = conf_file.get('name') or read_script_info(script_folder, '项目名称', os.path.splitext(conf_file['path'])[0] + '.js')
    desc = conf_file.get('desc') or read_script_info(script_folder, '使用声明', os.path.splitext(conf_file['path'])[0] + '.js')
    open_url = conf_file.get('openUrl') or read_script_info(script_folder, '下载地址', os.path.splitext(conf_file['path'])[0] + '.js')
    author = conf_file.get('author') or read_script_info(script_folder, '脚本作者', os.path.splitext(conf_file['path'])[0] + '.js')
    homepage = conf_file.get('homepage') or read_script_info(script_folder, '电报频道', os.path.splitext(conf_file['path'])[0] + '.js')
    icon = conf_file.get('icon') or ''
    date = conf_file.get('date') or read_script_info(script_folder, '更新日期', os.path.splitext(conf_file['path'])[0] + '.js')
    mitm = conf_file.get('MITM') or read_script_info(script_folder, '[MITM]', os.path.splitext(conf_file['path'])[0] + '.js')
    script = conf_file.get('Script') or read_script_info(script_folder, '[rewrite_local]', os.path.splitext(conf_file['path'])[0] + '.js')

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

def read_script_info(script_folder, keyword, script_filename):
    js_file_path = os.path.join(script_folder, script_filename)
    if os.path.exists(js_file_path):
        with open(js_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if keyword in line:
                    # 使用正则表达式匹配关键字后的内容
                    match = re.match(r'.*?\/\/.*?' + re.escape(keyword) + r'：(.+)', line)
                    if match:
                        return match.group(1).strip()
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
