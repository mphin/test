import os
import re
import requests

def ensure_directories_exist():
    directories = ['tmp', 'Script', 'plugin']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

if __name__ == "__main__":
    ensure_directories_exist()
    main()

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def generate_plugin_file(conf_file, script_folder, plugin_folder):
    conf_path = os.path.join(script_folder, conf_file)
    plugin_name = os.path.splitext(conf_file)[0] + ".plugin"

    with open(conf_path, 'r', encoding='utf-8') as conf_file:
        content = conf_file.read()

    name_match = re.search(r'#!name\s*=\s*(.*)', content)
    desc_match = re.search(r'#!desc\s*=\s*(.*)', content)
    openurl_match = re.search(r'#!openUrl\s*=\s*(.*)', content)
    author_match = re.search(r'#!author\s*=\s*(.*)', content)
    homepage_match = re.search(r'#!homepage\s*=\s*(.*)', content)
    icon_match = re.search(r'#!icon\s*=\s*(.*)', content)
    date_match = re.search(r'#!date\s*=\s*(.*)', content)
    mitm_match = re.search(r'\[MITM\]\s*=\s*(.*)', content, re.IGNORECASE)
    script_match = re.search(r'\[Script\]\s*=\s*(.*)', content, re.IGNORECASE)

    plugin_content = f'''#!name = {name_match.group(1) if name_match else get_value_from_script("项目名称", script_folder, conf_file)}
#!desc = {desc_match.group(1) if desc_match else get_value_from_script("使用声明", script_folder, conf_file)}
#!openUrl = {openurl_match.group(1) if openurl_match else get_value_from_script("下载地址", script_folder, conf_file)}
#!author = {author_match.group(1) if author_match else get_value_from_script("脚本作者", script_folder, conf_file)}
#!homepage = {homepage_match.group(1) if homepage_match else get_value_from_script("电报频道", script_folder, conf_file)}
#!icon = {icon_match.group(1) if icon_match else ""}
#!date = {date_match.group(1) if date_match else get_value_from_script("更新日期", script_folder, conf_file)}

[MITM]
{mitm_match.group(1) if mitm_match else get_value_from_script("[MITM]", script_folder, conf_file, True)}

[Script]
{script_match.group(1) if script_match else get_value_from_script("[rewrite_local]", script_folder, conf_file, True)}
'''

    plugin_path = os.path.join(plugin_folder, plugin_name)
    with open(plugin_path, 'w', encoding='utf-8') as plugin_file:
        plugin_file.write(plugin_content)

def get_value_from_script(key, script_folder, conf_file, is_block=False):
    script_path = os.path.join(script_folder, conf_file)
    with open(script_path, 'r', encoding='utf-8') as script_file:
        content = script_file.read()
    
    pattern = f'{key}：' if not is_block else f'{key}\n([\s\S]*?)(?=\[|$)'
    match = re.search(pattern, content, re.IGNORECASE)
    return match.group(1).strip() if match else ""

def main():
    tmp_folder = 'tmp'
    script_folder = 'Script'
    plugin_folder = 'plugin'

    for conf_file in os.listdir(tmp_folder):
        if conf_file.endswith('.conf'):
            conf_path = os.path.join(tmp_folder, conf_file)
            with open(conf_path, 'r', encoding='utf-8') as conf_file:
                download_url_match = re.search(r'#!url\s*=\s*(.*)', conf_file.read())
                if download_url_match:
                    download_url = download_url_match.group(1)
                    download_destination = os.path.join(script_folder, conf_file.name)
                    download_file(download_url, download_destination)
                    generate_plugin_file(conf_file, script_folder, plugin_folder)

def ensure_directories_exist():
    directories = ['tmp', 'Script', 'plugin']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

if __name__ == "__main__":
    ensure_directories_exist()
    main()
