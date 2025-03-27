# Imaris Convert

一个用于将图像转换为 Imaris 格式的 Python 工具包。

## 安装

```bash
pip install imaris-convert
```

## 使用方法

### 命令行使用

```bash
# 基本用法
imaris-convert input.tiff

# 指定输出目录
imaris-convert input.tiff -o /path/to/output/directory
```

### Python API 使用

```python
from imaris_convert import imaris_convert

# 转换图像文件
imaris_convert.convert_to_imaris(input_file, output_file)
```

## 依赖项

- Python >= 3.6
- numpy
- tifffile
- tqdm

## 许可证

MIT License 