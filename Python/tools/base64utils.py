# -*- coding: utf-8 -*-
"""
Created By Murray(m18527) on 2020/5/28 21:19
"""
import logging
import os
import re
from base64 import b64decode, b64encode
from io import BytesIO
from PIL import Image
from zlib import decompress

from fitz import fitz

try:
    from cPickle import loads, dumps
except ImportError:
    from pickle import loads, dumps

logger = logging.getLogger(__name__)


def base64_to_file(content, path):
    try:
        data = b64decode(content)
    except Exception as e:
        logger.error(e)
        raise e
    with open(path, 'wb') as f:
        f.write(data)


def dbsafe_decode(value, compress_object=False):
    if not value:
        return None
    value = value.encode()  # encode str to bytes
    value = b64decode(value)
    if compress_object:
        value = decompress(value)
    return loads(value)


def bytes_to_base64(content):
    try:
        base64_data = b64encode(content)
        base64_data = base64_data.decode("utf-8")
    except (Exception,) as e:
        logger.error(e)
        raise e
    return base64_data


def base64_to_bytes(b64, is_raise=True):
    try:
        b64 = b64decode(b64)
    except (Exception,) as e:
        logger.error(e)
        if is_raise:
            raise e
    return b64


def image_to_base64(image_path):
    img = Image.open(image_path)
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = b64encode(byte_data)
    return base64_str


def base64_to_image(base64_str, image_path=None):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    if image_path:
        img.save(image_path)
    return img

def pdf2image(path, img_outpath='', ext_name='png'):
    """
    将pdf转img保存，需要如下两个包
    pip install PyMuPDF
    pip install fitz
    :param path: pdf绝对路径或当前路径文件名
    :param img_outpath: imagepath default current path
    :param ext_name: extention name
    :return:
    """
    # 获取路径中的文件名
    filename = os.path.basename(path)
    # 没设置输出路径则与输入路径相同
    if not img_outpath:
        img_outpath = os.path.dirname(path)
    doc = fitz.Document(path)
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # PDF页数
        pix = page.get_pixmap()
        # 拼接路径文件名和拓展名
        save_path = os.path.join(img_outpath, ''.join(filename.rsplit('.', 1)[:-1]) + '_{}.'.format(page_num) + ext_name)
        pix.writeImage(save_path)
