import os
from pydub import AudioSegment
from subprocess import call


with open("submissions_to_render_demos.txt", 'r') as f:
    lines = f.readlines()

input_folder = './media/collabs/responses'
output_folder = './media/collabs/responses/demos'
submission_list_path = './submissions_to_render_demos.txt'

for line in lines:
    # Split the line into response ID and submission path
    response_id, submission_path = line.strip().split(',', 1)
    response_id = int(response_id)
    print(f"Processing: {submission_path} with ID: {response_id}")

    # Ensure the submission file exists
    if not os.path.exists(submission_path):
        print(f"File does not exist: {submission_path}")
        continue

    try:
        # Load the audio file
        audio = AudioSegment.from_file(submission_path)

        # Create the path for the low-quality MP3 with '_demo' appended to the file name
        file_name = os.path.basename(submission_path)
        base_name, ext = os.path.splitext(file_name)
        low_quality_name = f"{base_name}_demo.mp3"
        low_quality_path = os.path.join(output_folder, low_quality_name)

        # Export the audio file to low-quality MP3
        audio.export(low_quality_path, format="mp3", bitrate="64k")
        print(f"Saved low-quality MP3: {low_quality_path}")

        # Remove the processed entry from the list
        with open(submission_list_path, 'r') as f:
            lines = f.readlines()

        with open(submission_list_path, 'w') as f:
            for line in lines:
                if line.strip().split(',', 1)[1] != submission_path:
                    f.write(line)



        venv_activate_script = '../rmvenv/bin/activate'
        command = f'source {venv_activate_script} && python3 manage.py mark_demo_rendered {response_id} {low_quality_path}'

        # Use bash explicitly to ensure source is found
        call(f'bash -c "{command}"', shell=True)

    except Exception as e:
        print(f"Failed to process {submission_path}: {e}")

print("Processing complete.")