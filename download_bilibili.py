import subprocess


def download_bilibili_video(video_id, output_directory):
    output_template = f'{output_directory}/%(title)s-[{video_id}].%(ext)s'
    video_url = f'https://www.bilibili.com/video/{video_id}'
    subprocess.run(['yt-dlp', '-o', output_template, video_url])

def download_videos_from_file(file_path, output_directory):
    with open(file_path, 'r') as file:
        for line in file:
            video_id = line.strip()  
            if video_id:  
                download_bilibili_video(video_id, output_directory)
                print(f'Downloaded video {video_id} successfully to {output_directory}.')

if __name__ == '__main__':
    file_path = 'video_ids.txt'  
    output_directory = 'download' 
    download_videos_from_file(file_path, output_directory)
