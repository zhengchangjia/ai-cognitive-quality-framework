# simple-eval.py
# 简易评估脚本——将评估标准、素材和报告组合后发送给大模型

import os

def load_file(filepath):
    """读取文件内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def build_prompt(standard_path, material_path, report_path):
    """构建完整的评估提示词"""
    standard = load_file(standard_path)
    material = load_file(material_path)
    report = load_file(report_path)
    
    prompt = standard.replace(
        "{MATERIAL}", material
    ).replace(
        "{REPORT}", report
    )
    return prompt

def main():
    # 配置路径
    standard_path = "SPEC.md"
    material_path = "examples/example-01-material.md"
    report_path = "examples/example-01-report.md"
    
    # 构建提示词
    prompt = build_prompt(standard_path, material_path, report_path)
    
    # 输出提示词（你可以复制它发送给任何大模型）
    print(prompt)
    
    # 或者如果你有API密钥，可以直接调用
    # response = call_llm_api(prompt)
    # print(response)

if __name__ == "__main__":
    main()