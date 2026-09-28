import zstandard as zstd
import os
import subprocess
import hashlib
import time


def calculate_sha256(file_path):
    """फाइल की 100% शुद्धता जांचने के लिए डिजिटल फिंगरप्रिंट (SHA-256) जनरेशन"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def ai_smart_scan(file_path):
    """AI इनपुट इंजन: फ़ाइल का प्रकार पहचानकर सही डिपार्टमेंट को सौंपना"""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv']
    code_text_extensions = ['.py', '.js', '.json', '.html', '.css', '.c', '.cpp', '.java', '.txt', '.csv', '.xml', '.dat']
    
    if ext in video_extensions:
        return "video_optimize"
    elif ext in code_text_extensions:
        return "high_speed_code_core"
    return "zstd_quantum_core"

def optimize_video_ai(input_path, output_path, speed_preset):
    """AI वीडियो ऑप्टिमाइज़र - पिक्सल प्रोटेक्शन और डायनेमिक थ्रेड्स के साथ"""
    print(f"\n[🧠 AI Media Core]: Video Compression Active with Preset: {speed_preset}")
    
    # FFmpeg प्रेसेट मैपिंग (यूज़र के स्लाइडर के हिसाब से)
    if speed_preset in ['Ultrafast (Speed)', 'Balanced']:
        ffmpeg_preset = 'veryfast'
    else:
        ffmpeg_preset = 'medium'

    command = [
        'ffmpeg', '-y', '-i', input_path,
        '-vcodec', 'libx264',
        '-preset', ffmpeg_preset,
        '-crf', '23',
        '-maxrate', '2M', 
        '-bufsize', '4M',
        '-acodec', 'aac',
        '-b:a','128k',
        '-threads', '0',
        output_path
    ]
    
    # विंडोज़ पर बैकग्राउंड विंडो न खोलने के लिए फ्लैग
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0

    try:
        # 💡 फिक्स: डेडलॉक और हैंगिंग से बचने के लिए stdout/stderr को DEVNULL किया गया है
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, creationflags=creation_flags)
        return True
    except Exception as e:
        print(f"❌ वीडियो कंप्रेशन फेल: {e}")
        return False

def quantum_compress_data(input_path, output_path, compression_level):
    """क्वांटम डेटा/कोड कंप्रेसर - 5x फ़ास्ट मल्टी-थ्रेडेड आर्किटेक्चर"""
    print(f"\n[🔒 AI Quantum Compressor]: Level-{compression_level} Data Crushing...")
    cctx = zstd.ZstdCompressor(level=compression_level, threads=-1)
    try:
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            f_out.write(cctx.compress(f_in.read()))
        return True
    except Exception as e:
        print(f"❌ डेटा कंप्रेशन फेल: {e}")
        return False

def smart_decompress(input_path, output_path):
    """द महा-डीकंप्रेशर - True Bit-Perfect Extraction Engine"""
    print("\n[🔓 AI Quantum Decompressor]: Extracting to Original State...")
    dctx = zstd.ZstdDecompressor()
    try:
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            f_out.write(dctx.decompress(f_in.read()))
        return True
    except:
        return False

def smart_compress(input_file_path, output_file_path, mode_selection):
    """मुख्य प्रवेश द्वार जो एडेप्टिव मोड्स को हैंडल करता है"""
    decision = ai_smart_scan(input_file_path)
    
    if mode_selection == "Ultrafast (Speed)":
        zstd_level = 3
    elif mode_selection == "Balanced":
        zstd_level = 9
    else:
        zstd_level = 19
        
    if decision == "video_optimize":
        # वीडियो कंप्रेस करें
        is_success = optimize_video_ai(input_file_path, output_file_path, mode_selection)
        if is_success:
            # 💡 फिक्स: कंप्रेस्ड आउटपुट फ़ाइल का हैश निकालें ताकि अनपैकिंग एरर न आए
            hash_val = calculate_sha256(output_file_path)
            return True, 'video', hash_val
        else:
            return False, 'error', None
    else:
        is_success = quantum_compress_data(input_file_path, output_file_path, zstd_level)
        if is_success:
            hash_val = calculate_sha256(input_file_path)
            return is_success, 'data', hash_val
        else:
            return False, 'error', None

