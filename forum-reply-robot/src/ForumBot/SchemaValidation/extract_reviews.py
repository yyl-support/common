# version：1.0.31

import re


def is_redfish_related(title, content):
    """
    检查评审点是否与 Redfish 相关
    通过检查标题和内容是否包含 "redfish" 关键字（不区分大小写）
    """
    title_lower = title.lower() if title else ''
    content_lower = content.lower() if content else ''
    return 'redfish' in title_lower or 'redfish' in content_lower


def extract_review_points_from_html(html_content):
    """
    通用的评审点提取函数，不依赖特定HTML格式
    通过关键词"评审点"定位，然后解析所在标签的内容

    规则：只提取明确标记为"评审点1"、"评审点2"等的标题，
          不提取纯编号列表（1、2、3等）
          只提取与 Redfish 相关的评审点
    """
    review_points = []
    lines = html_content.split('\n')

    # 查找包含"评审点N"标题的行（单行匹配，避免跨行误匹配）
    i = 0
    while i < len(lines):
        line = lines[i]

        # 单行检查：只匹配同一行内的"评审点N"
        if '评审点' in line:
            # 检查是否包含"评审点N"（N是数字），且在同一行内
            match = re.search(r'评审点\s*\d+[：:：]?', line)
            if match:
                # 检查是否是标题行（行首、或##/<h3>标记后）
                stripped = line.lstrip()
                is_title = (
                    stripped.startswith('##') or  # markdown标题
                    stripped.startswith('<h') or  # HTML标题
                    stripped.startswith('评审点')  # 直接以"评审点"开头
                )
                if is_title:
                    # 提取标题
                    title = line

                    # 移除markdown标记
                    title = re.sub(r'^###?\s*', '', title)
                    title = re.sub(r'^<h[34]>\s*', '', title, flags=re.IGNORECASE)
                    title = re.sub(r'\s*</h[34]>\s*$', '', title, flags=re.IGNORECASE)
                    title = re.sub(r'\[\]\([^\)]*\)', '', title)  # 移除 []() anchor
                    title = re.sub(r'<[^>]+>', '', title)  # 移除HTML标签
                    title = title.strip()

                    if title.startswith('评审点'):
                        # 提取内容：收集到下一个评审点或章节标题之前的所有内容
                        content_lines = []
                        j = i + 1

                        while j < len(lines):
                            next_line = lines[j]

                            # 遇到新的评审点、章节标题或文档末尾则停止
                            # 单行检查，避免跨行误匹配
                            if re.search(r'评审点\s*\d+[：:：]?', next_line):
                                next_stripped = next_line.lstrip()
                                if (next_stripped.startswith('##') or
                                    next_stripped.startswith('<h') or
                                    next_stripped.startswith('评审点')):
                                    break

                            if re.match(r'^##+\s+\[?\]?\(', next_line):  # markdown标题
                                break
                            if re.match(r'^<h[234]', next_line, re.IGNORECASE):  # HTML标题
                                break
                            if next_line.strip() in ['评审结论', '遗留问题', '背景', '评审方案', '评审依据', '详细描述']:
                                break

                            content_lines.append(next_line)
                            j += 1

                        # 合并并清理内容
                        content = '\n'.join(content_lines)
                        content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)
                        content = re.sub(r'\`([^`]+)\`', r'\1', content)
                        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
                        content = re.sub(r'<[^>]+>', ' ', content)
                        content = re.sub(r'\s+', ' ', content).strip()

                        # 检查是否与 Redfish 相关
                        if is_redfish_related(title, content):
                            if content or title:  # 即使没有内容也保留标题
                                review_points.append({'title': title, 'content': content})

                        i = j - 1  # 跳过已处理的内容行
        i += 1

    return review_points
