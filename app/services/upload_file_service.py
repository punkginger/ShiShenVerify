import os
from werkzeug.utils import secure_filename
from config import Config

class UploadFileService:
    @staticmethod
    def upload(file):
        filename = secure_filename(file.filename)
        upload_folder = Config.UPLOAD_FOLDER

        # 获取文件拓展名
        _, extension = os.path.splitext(filename)

        # 根据拓展名获取目标目录
        target_dir = UploadFileService.get_target_directory(extension)

        # 如果目标目录不存在，则创建
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # 生成保存文件的完整路径
        file_path = os.path.join(target_dir, filename)

        # 保存文件
        file.save(file_path)

        # 返回文件的完整路径
        return file_path

    @staticmethod
    def get_target_directory(extension):
        # 定义不同拓展名对应的目标目录
        target_directories = {
            ".jpg": "images",
            ".png": "images",
            ".mp4": "videos",
            ".wav": "audio",
            ".txt": "text"
            # 添加其他拓展名及对应的目标目录
        }

        # 获取拓展名对应的目标目录，如果没有对应的目录则使用默认目录
        return os.path.join(upload_folder, target_directories.get(extension, "misc"))
