from concurrent.futures import ProcessPoolExecutor, as_completed
import cv2
import multiprocessing
import os
import sys
import shutil
import moviepy.editor as meditor
import math
import time
import datetime
#from tqdm import tqdm
#from setup import feature_vector
#from scipy import spatial
args=sys.argv
try:
    shutil.rmtree(args[2])
    #shutil.rmtree('vis/imgs')
    #os.mkdir('vis/imgs')
    #print(1)
except:
    pass

def print_progress(iteration, total, prefix='', suffix='', decimals=3, bar_length=100):
    #Call in a loop to create standard out progress bar
    #:param iteration: current iteration
    #:param total: total iterations
    #:param prefix: prefix string
    #:param suffix: suffix string
    #:param decimals: positive number of decimals in percent complete
    #:param bar_length: character length of bar
    #:return: None


    format_str = "{0:." + str(decimals) + "f}"  # format the % done number string
    percents = format_str.format(100 * (iteration / float(total)))  # calculate the % done
    filled_length = int(round(bar_length * iteration / float(total)))  # calculate the filled bar length
    bar = '#' * filled_length + '-' * (bar_length - filled_length)  # generate the bar string
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),  # write out the bar
    sys.stdout.flush()  # flush to stdout
def extract_frames(video_path, frames_dir, overwrite=False, start=-1, end=-1, every=5,l=1):
    
    #Extract frames from a video using OpenCVs VideoCapture
    #:param video_path: path of the video
    #:param frames_dir: the directory to save the frames
    #:param overwrite: to overwrite frames that already exist?
    #:param start: start frame
    #:param end: end frame
    #:param every: frame spacing
    #:return: count of images saved
    
    video_path = os.path.normpath(video_path)  # make the paths OS (Windows) compatible
    frames_dir = os.path.normpath(frames_dir)  # make the paths OS (Windows) compatible

    video_dir, video_filename = os.path.split(video_path)  # get the video path and filename from the path

    assert os.path.exists(video_path)  # assert the video file exists

    capture = cv2.VideoCapture(video_path)  # open the video using OpenCV

    if start < 0:  # if start isn't specified lets assume 0
        start = 0
    if end < 0:  # if end isn't specified assume the end of the video
        end = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    capture.set(1, start)  # set the starting frame of the capture
    frame = start  # keep track of which frame we are up to, starting from start
    while_safety = 0  # a safety counter to ensure we don't enter an infinite while loop (hopefully we won't need it)
    saved_count = 0  # a count of how many frames we have saved
    #if count==0:
     #   t=0
    #else:
     #   t=1
    #l=True
    while frame < end:  # lets loop through the frames until the end
        
        _, image = capture.read()  # read an image from the capture
        if while_safety > 500:  # break the while if our safety maxs out at 500
            break

        # sometimes OpenCV reads None's during a video, in which case we want to just skip
        if image is None:  # if we get a bad return flag or the image we read is None, lets not save
            while_safety += 1  # add 1 to our while safety, since we skip before incrementing our frame variable
            continue  # skip

        if frame % (every*l) == 0:
            #print(1)
            while_safety = 0
            #if t==0:
             #   threshold=feature_vector(image)
            #print(threshold)
            #x=feature_vector(image)
            #cos=1-spatial.distance.cosine(threshold,x)
            #if cos>=0.9 and t!=0:
             #   l=False
            #else:
             #   l=True
              #  threshold=x
            #os.mkdir(frames_dir+'/'+video_filename)
            # save=str(datetime.timedelta(seconds=int(frame/every)))
            # save.replace(":","-")
            timestamp = math.floor(frame/every)
            seconds = timestamp % 60
            timestamp = timestamp/60
            minutes = timestamp % 60
            timestamp = timestamp/60
            hours = timestamp%60     
            #cv2.imwrite('./data/'+str(math.floor(hours))+"-"+str(math.floor(minutes))+"-"+str(math.floor(seconds))+'.jpg',frame)
            save = str(math.floor(hours))+"-"+str(math.floor(minutes))+"-"+str(math.floor(seconds))
            save_path = os.path.join(frames_dir,"{}.jpg".format(save))
            if not os.path.exists(save_path) or overwrite:  # if it doesn't exist or we want to overwrite anyways
                cv2.imwrite(save_path, image)

                  # save the extracted image
                saved_count += 1
        
                  # increment our counter by one

        frame += 1  # increment our frame count
    capture.release()  # after the while has finished close the capture

    return saved_count  # and return the count of the images we saved


def video_to_frames(video_path, frames_dir, overwrite=False,chunk_size=1000,l=1):
    #Extracts the frames from a video using multiprocessing
    #:param video_path: path to the video
    #:param frames_dir: directory to save the frames
   # :param overwrite: overwrite frames if they exist?
    #:param every: extract every this many frames
    #:param chunk_size: how many frames to split into chunks (one chunk per cpu core process)
    #:return: path to the directory where the frames were saved, or None if fails
    
    video_path = os.path.normpath(video_path)  # make the paths OS (Windows) compatible
    frames_dir = os.path.normpath(frames_dir)  # make the paths OS (Windows) compatible

    video_dir, video_filename = os.path.split(video_path)  # get the video path and filename from the path

    # make directory to save frames, its a sub dir in the frames_dir with the video name
    os.makedirs(frames_dir, exist_ok=True)

    capture = cv2.VideoCapture(video_path)  # load the video
    total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))  # get its total frame count
    #print(total)
    capture.release()  # release the capture straight away
    video = meditor.VideoFileClip(video_path)
    video_duration = int(video.duration)
    every=(math.ceil(total/video_duration))
    print(every)
    #print(every)
    if total < 1:  # if video has no frames, might be and opencv error
        print("Video has no frames. Check your OpenCV + ffmpeg installation")
        return None  # return None

    frame_chunks = [[i, i+chunk_size] for i in range(0, total, chunk_size)]  # split the frames into chunk lists
    frame_chunks[-1][-1] = min(frame_chunks[-1][-1], total-1)  # make sure last chunk has correct end frame, also handles case chunk_size < total

    prefix_str = "Extracting frames from {}".format(video_filename)  # a prefix string to be printed in progress bar
    count=0
    # execute across multiple cpu cores to speed up processing, get the count automatically
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:

        futures = [executor.submit(extract_frames,video_path, frames_dir, overwrite, f[0], f[1],every,l)
                   for f in frame_chunks]  # submit the processes: extract_frames(...)
        for i, f in enumerate(as_completed(futures)):  # as each process completes
            print_progress(i, len(frame_chunks)-1, prefix=prefix_str, suffix='Complete')  
    return os.path.join(frames_dir, video_filename)
start=time.time()
video_to_frames(video_path=args[1], frames_dir=args[2], overwrite=True, chunk_size=1000,l=10)
print(time.time()-start)
