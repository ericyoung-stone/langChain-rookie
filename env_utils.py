from dotenv import load_dotenv
import os

def load_environment_variables(env_path: str = None):
    """加载环境变量配置文件"""
    if env_path:
        dotenv_path = env_path
    else:
        try:
            # __file__: 这是一个内置变量，表示当前 Python 脚本的文件路径。
            print(f'__file__: {__file__}')  # 检查 __file__ 是否存在, os.path.dirname() 可以返回指定路径的父目录
            dotenv_path = os.path.join(os.path.normpath(os.path.dirname(__file__)), '.env')
            print(f'dotenv_path1: {dotenv_path}')
        except NameError as e:
            print(f'NameError: {e}')
            print("Running in an interactive environment, using current directory instead.")
            # 使用 os.path.join() 和 .. 返回指定路径的父目录
            cur_work_dir = os.getcwd()
            print(cur_work_dir)
            dotenv_path = os.path.normpath(os.path.join(cur_work_dir, '..', '.env'))
            print(f'dotenv_path2: {dotenv_path}')
    # 原有调用逻辑保持不变
    ok = load_dotenv(dotenv_path)
    if ok:
        print(f'load env ok')
    else:
        print(f'load env fail')