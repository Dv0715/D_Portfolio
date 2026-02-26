import os
import subprocess

def convert_mp4_to_webm(input_folder):
    # 如果輸出資料夾不存在則建立
    output_folder = os.path.join(input_folder, "converted_webm")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 支援的影片格式
    valid_extensions = ('.mp4', '.mov', '.m4v')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.webm")

            print(f"正在轉換 (高品質/無聲): {filename}...")

            # FFmpeg 指令
            command = [
                'ffmpeg', '-i', input_path,
                '-c:v', 'libvpx-vp9',
                '-crf', '22',           # 高品質設定（15-20 非常清晰）
                '-b:v', '0', 
                '-an',                  # 關鍵：移除音軌
                '-deadline', 'good',    # 兼顧品質與速度
                '-cpu-used', '2',       # 增加運算精細度
# 強制使用不含透明通道的格式，有助於進一步壓縮體積
                '-pix_fmt', 'yuv420p',
                output_path,
                '-y'                    # 直接覆蓋舊檔
            ]

            try:
                # 執行轉換
                subprocess.run(command, check=True)
                print(f"成功: {output_path}")
            except subprocess.CalledProcessError as e:
                print(f"轉換 {filename} 時出錯: {e}")

if __name__ == "__main__":
    # 輸入路徑時，直接按 Enter 會處理當前資料夾
    user_input = input("請輸入影片資料夾路徑 (直接按 Enter 代表當前路徑): ").strip('"').strip()
    path = user_input if user_input else "." 
    convert_mp4_to_webm(path)
    print("\n所有高品質無聲轉換任務已完成！")