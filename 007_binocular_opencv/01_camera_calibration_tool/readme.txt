标定
python3 calibration.py --image_size 1280x720 --mode calibrate --corner 9x6 --square 24

矫正视频
python3 calibration.py --image_size 1280x720 --mode rectify --video_path cD.avi

说明：
--corner 9x6 说明格子是10列7行