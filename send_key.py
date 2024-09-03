import win32gui
import win32con
import win32api
import time
import threading

def send_enter_key(hwnd):
    print("Sending Enter key...")
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.05)  # Small delay to mimic a real key press
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    print("Enter key sent successfully.")

def main():
    # Find the window handle for Diablo IV (English, Simplified Chinese, Traditional Chinese)
    hwnd = (win32gui.FindWindow(None, "Diablo IV") or
            win32gui.FindWindow(None, "暗黑破坏神IV") or
            win32gui.FindWindow(None, "《暗黑破壞神 IV》"))
    
    if hwnd:
        print("Found Diablo IV window. Bringing it to the foreground...")
        win32gui.SetForegroundWindow(hwnd)
        
        # Create a new thread for sending the key
        key_thread = threading.Thread(target=send_enter_key, args=(hwnd,))
        key_thread.start()
        
        print("Main thread continues execution...")
    else:
        print("Diablo IV window not found.")

if __name__ == "__main__":
    main()
