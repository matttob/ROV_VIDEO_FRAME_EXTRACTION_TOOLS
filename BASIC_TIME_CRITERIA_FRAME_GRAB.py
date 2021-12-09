import cv2
import math

# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()
parser.add_argument('start_time_mins',type=int)
parser.add_argument('start_time_secs',type=int)
parser.add_argument('end_time_mins',type=int)
parser.add_argument('end_time_secs',type=int)
parser.add_argument('frame_interval',type=int)
parser.add_argument('video_file',type=str)
parser.add_argument('image_folder',type=str)

args = parser.parse_args()


# Read the video from specified path this could clearly be changed to a file open box
cap = cv2.VideoCapture(args.video_file)  
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate=cap.get(cv2.CAP_PROP_FPS)


start_frame=math.floor((args.start_time_mins*60*frame_rate)+(args.start_time_secs*frame_rate))
end_frame=math.floor((args.end_time_mins*60*frame_rate)+(args.end_time_secs*frame_rate))

# Loop through specified frames 
for i in range(start_frame, end_frame, args.frame_interval):
    
    # choose specified frame
    cap.set(cv2.CAP_PROP_POS_FRAMES,i)
    # read specified frame
    ret, frame = cap.read()

    # save cropped image in image folder
    # write specified frame to jpg image
    # create time stamp for frame file name
    fractional_mins, whole_mins = math.modf((i/frame_rate)/60)
    # create and save jpegs
    cv2.imwrite(args.image_folder + 'Frame_'+str(i) + '_' + str(round(whole_mins)) + 'mins' + '_' + str(round(fractional_mins*60)) + 'secs' + '.jpg',frame)

        