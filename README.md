# OpenAI Whisper Playground

This playground to get fast running with [OpenAI Whisper speech 2 text](https://github.com/openai/whisper).

## FFmpeg

ffmpeg must be installed, check by running in the CMD.

``` shell
ffmpeg -version
```

## Conda Install

``` shell
conda remove --name whisper --all -y
conda create --name whisper python=3.11.9 pytorch-cuda=12.4 pytorch cudatoolkit -c pytorch -c nvidia -y
conda activate whisper
pip install -U openai-whisper
pip install ffmpeg-python
conda install -c conda-forge ffmpeg
```
