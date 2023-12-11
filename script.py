import os
import re
import shutil

# 定义文件夹路径
tmp_folder = "tmp"
script_folder = "Script"
plugin_folder = "plugin"

# 创建plugin文件夹
if not os.path.exists(plugin_folder):
    os.makedirs(plugin_folder)

# 遍历tmp文件夹中的conf后缀文件
for filename in os.listdir(tmp_folder):
    if filename.endswith(".conf"):
        conf_file_path = os.path.join(tmp_folder, filename)
        plugin_file_path = os.path.join(plugin_folder, filename.replace(".conf", ".plugin"))

        # 读取conf文件内容
        with open(conf_file_path, "r", encoding="utf-8") as conf_file:
            conf_content = conf_file.read()

        # 提取各项信息
        name_match = re.search(r'#!name = (.+)', conf_content)
        name = name_match.group(1).strip() if name_match else None

        desc_match = re.search(r'#!desc = (.+)', conf_content)
        desc = desc_match.group(1).strip() if desc_match else None

        openUrl_match = re.search(r'#!openUrl = (.+)', conf_content)
        openUrl = openUrl_match.group(1).strip() if openUrl_match else None

        author_match = re.search(r'#!author = (.+)', conf_content)
        author = author_match.group(1).strip() if author_match else None

        homepage_match = re.search(r'#!homepage = (.+)', conf_content)
        homepage = homepage_match.group(1).strip() if homepage_match else None

        icon_match = re.search(r'#!icon = (.+)', conf_content)
        icon = icon_match.group(1).strip() if icon_match else None

        date_match = re.search(r'#!date = (.+)', conf_content)
        date = date_match.group(1).strip() if date_match else None

        mitm_match = re.search(r'\[MITM\]\n(.+)', conf_content, re.DOTALL | re.IGNORECASE)
        mitm = mitm_match.group(1).strip() if mitm_match else None

        script_match = re.search(r'\[Script\]\n(.+)', conf_content, re.DOTALL | re.IGNORECASE)
        script = script_match.group(1).strip() if script_match else None

        # 如果信息为空，则从下载文件中提取
        if not name:
            name_match = re.search(r'项目名称：(.+)', conf_content)
            name = name_match.group(1).strip() if name_match else None

        if not desc:
            desc_match = re.search(r'使用声明：(.+)', conf_content)
            desc = desc_match.group(1).strip() if desc_match else None

        if not openUrl:
            openUrl_match = re.search(r'下载地址：(.+)', conf_content)
            openUrl = openUrl_match.group(1).strip() if openUrl_match else None

        if not author:
            author_match = re.search(r'脚本作者：(.+)', conf_content)
            author = author_match.group(1).strip() if author_match else None

        if not homepage:
            homepage_match = re.search(r'电报频道：(.+)', conf_content)
            homepage = homepage_match.group(1).strip() if homepage_match else None

        if not date:
            date_match = re.search(r'更新日期：(.+)', conf_content)
            date = date_match.group(1).strip() if date_match else None

        if not mitm:
            mitm_match = re.search(r'\[MITM\]\n(.+)', conf_content, re.DOTALL | re.IGNORECASE)
            mitm = mitm_match.group(1).strip() if mitm_match else None

        if not script:
            script_match = re.search(r'\[rewrite_local\]\n(.+)', conf_content, re.DOTALL | re.IGNORECASE)
            script = script_match.group(1).strip() if script_match else None

        # 生成plugin文件内容
        plugin_content = f'''#!name = {name}
#!desc = {desc}
#!openUrl = {openUrl}
#!author = {author}
#!homepage = {homepage}
#!icon = {icon}
#!date = {date}

[MITM]
{mitm}

[Script]
{script}
'''

        # 写入plugin文件
        with open(plugin_file_path, "w", encoding="utf-8") as plugin_file:
            plugin_file.write(plugin_content)

        # 将下载文件拷贝到Script文件夹
        shutil.copy(openUrl, os.path.join(script_folder, f"{filename.replace('.conf', '')}.js"))

print("工作流脚本执行完毕。")
