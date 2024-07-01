import cv2
import os
import time

def record_rtsp_stream(rtsp_url, duration, output_file, fps=30):
    try:

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        
        cap = cv2.VideoCapture(rtsp_url)
        
        if not cap.isOpened():
            print(f"Error: Unable to open video stream from {rtsp_url}")
            return
        
        
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
        
        start_time = time.time()
        
        while int(time.time() - start_time) < duration:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame from stream")
                break
            out.write(frame)
        
        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        print(f"Recording saved to {output_file}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    rtsp_url = "rtsp://Cam1:Etcop@2023Ai1@cam8ocd.cameraddns.net:556/Streaming/Channels/1"
    duration = 30  
    output_file = os.path.join(os.path.abspath("."), "video", "night_output.mp4")
    
    record_rtsp_stream(rtsp_url, duration, output_file)
