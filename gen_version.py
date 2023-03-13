# -*- coding: utf-8 -*-
# @Author   : KaiShin
# @Time     : 2023/3/3

import os
import subprocess

import toml

conf_name = "./pyproject.toml"

# 读取 toml 文件
with open(conf_name, "r") as f:
    config = toml.load(f)

# 获取git版本
command1 = ["git", "describe", "--tags", "--always"]
command2 = ["sed", "s/-g.*$//"]
result1 = subprocess.run(command1, stdout=subprocess.PIPE, check=True, encoding="utf-8")
result2 = subprocess.run(command2, input=result1.stdout, stdout=subprocess.PIPE, check=True, encoding="utf-8")
git_version = result2.stdout.strip()
print(f"git_version1：{git_version}")

# 获取push type
git_ref = os.getenv("GITHUB_REF", "refs/heads")
print(f"git_ref: {git_ref}")

# modify
proj_name = config["tool"]["poetry"]["name"]
if git_ref.startswith("refs/tags"):
    # 发行版
    flag = "post"
else:
    # 开发版
    flag = "dev"
    config["tool"]["poetry"]["name"] = f"{proj_name}-{flag}"

git_version = git_version.replace("-", flag)
print(f"build_version:{git_version}")
print(f"project_name:{config['tool']['poetry']['name']}")


# 修改属性值
config["tool"]["poetry"]["version"] = git_version

# 写回 toml 文件
with open(conf_name, "w") as f:
    toml.dump(config, f)

if __name__ == "__main__":
    pass
