import os
from PIL import Image

def convert_to_webp():
    # 取得當前資料夾路徑
    current_dir = os.getcwd()
    print(f"開始掃描路徑: {current_dir}")

    # 設定要掃描的副檔名
    target_extensions = ('.jpg', '.jpeg', '.png')
    count = 0

    # 遞迴掃描所有子資料夾
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.lower().endswith(target_extensions):
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]
                output_path = os.path.join(root, f"{file_name}.webp")

                try:
                    with Image.open(file_path) as img:
                        # 保持原始長寬，僅轉換格式
                        # quality=90 是高畫質壓縮平衡點，lossless=False 適合相片
                        img.save(output_path, "WEBP", quality=90)
                        
                    print(f"成功: {file} -> {file_name}.webp")
                    count += 1
                except Exception as e:
                    print(f"錯誤: 無法轉換 {file}，原因: {e}")

    print(f"\n--- 轉換完成！共處理 {count} 個檔案 ---")
    print("提示：確認 .webp 檔案沒問題後，可手動刪除原有的 .jpg 和 .png 檔案。")

if __name__ == "__main__":
    convert_to_webp()