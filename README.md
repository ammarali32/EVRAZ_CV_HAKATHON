# EVRAZ_CV_HAKATHON
This repository contains training and inference scripts for the EVRAS track 2 (computer vision) solution by Ammar Ali.
# Installation and Running
## Option 1
* <!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">pip install <span style="color: #333333">-</span>r requirements<span style="color: #333333">.</span>txt
</pre></div>
* Download weights from <a href="https://drive.google.com/file/d/18hpJEH3Im2656Q5PZ8P39MMe_i_uOvI2/view?usp=sharing">here</a>
* <!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">python run<span style="color: #333333">.</span>py <span style="color: #333333">--</span>weights weights_path <span style="color: #333333">--</span>data images_path <span style="color: #333333">--</span>output output<span style="color: #333333">-</span><span style="color: #007020">dir</span> <span style="color: #333333">--</span>sub_sample sample_submission<span style="color: #333333">.</span>json <span style="color: #333333">--</span>imgsz image_size
</pre></div>
## Option 2
* <!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">docker build .
</pre></div>
* <a href = "https://docs.docker.com/get-docker/"> Docker Installation Guide</a>
# Note
Don't forget to download the <a href="https://disk.yandex.ru/d/fKjGJTI91TWCNA">data</a>
