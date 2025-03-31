# -*- coding: utf-8 -*-
import sys
import io
import os
import json
from html import escape

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_hidden_links_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"文件 {input_file} 未找到。请确保文件存在并且路径正确。")
        return

    html_content = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>隐藏的网址链接</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .link-container { margin-bottom: 10px; }
        .hidden-link { cursor: pointer; color: blue; text-decoration: underline; }
    </style>
    <script>
        function redirectTo(url) { window.location.href = url; }
    </script>
</head>
<body>
    <h1>隐藏的网址链接</h1>
    <div id="links">
'''

    for index, url in enumerate(urls, start=1):
        link_id = index
        escaped_url = escape(url)  # 转义HTML内容
        json_url = json.dumps(url)  # 生成安全的JSON字符串
        html_content += f'        <div class="link-container">\n'
        html_content += f'            <span id="link-{link_id}" class="hidden-link" onclick=\'redirectTo({json_url})\'>{escaped_url}</span>\n'
        html_content += '        </div>\n'

    html_content += '''
    </div>
</body>
</html>
'''

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML文件已成功创建并保存为 {output_file}")
    except Exception as e:
        print(f"写入文件时出错: {e}")

if __name__ == "__main__":
    input_filename = "urls.txt"
    output_filename = "hidden_links.html"

    if not os.path.exists(input_filename):
        print(f"输入文件 {input_filename} 不存在。")
    else:
        create_hidden_links_html(input_filename, output_filename)