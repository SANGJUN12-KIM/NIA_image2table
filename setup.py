from setuptools import setup, find_packages

setup(
    name='NIA_image2table',
    version='1.0',
    description='Extract text from tables in images.',
    author='Bae Yong Bin',
    author_email='mame-mame@kakao.com',
    url='',
    download_url='',
    install_requires=['numpy', 'torch', 'torchvision', 'opencv-python'],
    packages=find_packages(),
    keywords=['Extract_text', 'table_ocr', 'easyOCR'],
    python_requires='==3.8',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ],
)