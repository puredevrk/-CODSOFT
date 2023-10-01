# # # import tkinter as tk
# # # from tkinter import simpledialog, messagebox
# # # import time
# # # import winsound

# # # class AlarmClock:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("Alarm Clock")
        
# # #         self.alarms = []
        
# # #         self.current_time_label = tk.Label(root, font=("Helvetica", 48))
# # #         self.current_time_label.pack(pady=20)
        
# # #         self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
# # #         self.set_alarm_button.pack(pady=10)
        
# # #         self.alarm_listbox = tk.Listbox(root)
# # #         self.alarm_listbox.pack(pady=10)
        
# # #         self.dismiss_button = tk.Button(root, text="Dismiss", command=self.dismiss_alarm)
# # #         self.dismiss_button.pack(pady=10)
        
# # #         self.update_time()
# # #         self.check_alarms()
    
# # #     def update_time(self):
# # #         current_time = time.strftime("%H:%M:%S %p")
# # #         self.current_time_label.config(text=current_time)
# # #         self.root.after(1000, self.update_time)
    
# # #     def set_alarm(self):
# # #         alarm_time = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM AM/PM):")
# # #         # Parse alarm_time and add it to the self.alarms list
# # #         period = period.lower()
# # #         if alarm_time:
# # #         # Parse alarm_time and add it to the self.alarms list
        
# # #             if period.lower() == 'am':
# # #                 hours = int(hours) % 12
# # #             else:
# # #                 hours = (int(hours) % 12) + 12
# # #         alarm_data = {
# # #             "time": f"{hours:02d}:{minutes} {period.upper()}",
# # #             "active": True  # You can set the alarm as active by default
# # #         }
# # #         self.alarms.append(alarm_data)
# # #         self.alarm_listbox.insert(tk.END, alarm_data["time"])
        
# # #     def check_alarms(self):
# # #         current_time = time.strftime("%H:%M %p")
# # #         for alarm in self.alarms:
# # #             if alarm["time"] == current_time and alarm["active"]:
# # #                 winsound.PlaySound("alarm_sound.wav", winsound.SND_FILENAME)
# # #                 response = messagebox.askquestion("Alarm", "Alarm! Snooze?")
# # #                 if response == 'yes':
# # #                     # Implement snooze functionality
# # #                     pass
# # #                 else:
# # #                     self.dismiss_alarm()
# # #         self.root.after(1000, self.check_alarms)
    
# # #     def dismiss_alarm(self):
# # #         winsound.PlaySound(None, winsound.SND_PURGE)  # Stop the alarm sound
# # #         # Implement dismiss functionality
# # #         selected_alarm_index = self.alarm_listbox.curselection()
    
# # #     # Ensure an alarm is selected before attempting to dismiss
# # #         if selected_alarm_index:
# # #             selected_alarm_index = int(selected_alarm_index[0])
# # #             dismissed_alarm = self.alarms[selected_alarm_index]
            
# # #             # Implement dismiss functionality, for example:
# # #             # 1. Remove the dismissed alarm from the alarms list
# # #             self.alarms.pop(selected_alarm_index)
            
# # #             # 2. Remove the dismissed alarm from the listbox
# # #             self.alarm_listbox.delete(selected_alarm_index)
            
# # #             # 3. Optionally display a message indicating the alarm was dismissed
# # #             messagebox.showinfo("Dismissed", f"Dismissed Alarm: {dismissed_alarm['time']}")
# # #         pass

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = AlarmClock(root)
# # #     root.mainloop()
# # import tkinter as tk
# # from tkinter import simpledialog, messagebox
# # import time
# # import winsound

# # class AlarmClock:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Alarm Clock")
# #         self.root.configure(bg="blue")  # Set background color to blue
        
# #         self.alarms = []
        
# #         self.current_time_label = tk.Label(root, font=("Helvetica", 48), bg="blue", fg="white")
# #         self.current_time_label.pack(pady=20)
        
# #         self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
# #         self.set_alarm_button.pack(pady=10)
        
# #         self.alarm_listbox = tk.Listbox(root)
# #         self.alarm_listbox.pack(pady=10)
        
# #         self.dismiss_button = tk.Button(root, text="Dismiss", command=self.dismiss_alarm)
# #         self.dismiss_button.pack(pady=10)
        
# #         self.update_time()
# #         self.check_alarms()
    
# #     def update_time(self):
# #         current_time = time.strftime("%H:%M:%S %p")
# #         self.current_time_label.config(text=current_time)
# #         self.root.after(1000, self.update_time)
    
# #     def set_alarm(self):
# #         alarm_time = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM AM/PM):")
# #         alarm_date = simpledialog.askstring("Set Alarm", "Enter alarm date (MM/DD/YYYY):")
# #         if alarm_time and alarm_date:
# #             hours, minutes, period = map(str.strip, alarm_time.split(':'))
# #             month, day, year = map(str.strip, alarm_date.split('/'))
# #             period = period.lower()
# #             if period == 'am':
# #                 hours = int(hours) % 12
# #             else:
# #                 hours = (int(hours) % 12) + 12
# #             alarm_data = {
# #                 "time": f"{month}/{day}/{year} {hours:02d}:{minutes} {period.upper()}",
# #                 "active": True  # You can set the alarm as active by default
# #             }
# #             self.alarms.append(alarm_data)
# #             self.alarm_listbox.insert(tk.END, alarm_data["time"])
        
# #     def check_alarms(self):
# #         current_time = time.strftime("%m/%d/%Y %H:%M %p")
# #         for alarm in self.alarms:
# #             if alarm["time"] == current_time and alarm["active"]:
# #                 winsound.PlaySound("alarm_sound.wav", winsound.SND_FILENAME)
# #                 response = messagebox.askquestion("Alarm", "Alarm! Snooze?")
# #                 if response == 'yes':
# #                     # Implement snooze functionality
# #                     pass
# #                 else:
# #                     self.dismiss_alarm()
# #         self.root.after(1000, self.check_alarms)
    
# #     def dismiss_alarm(self):
# #         winsound.PlaySound(None, winsound.SND_PURGE)  # Stop the alarm sound
# #         selected_alarm_index = self.alarm_listbox.curselection()
# #         if selected_alarm_index:
# #             selected_alarm_index = int(selected_alarm_index[0])
# #             dismissed_alarm = self.alarms[selected_alarm_index]
# #             self.alarms.pop(selected_alarm_index)
# #             self.alarm_listbox.delete(selected_alarm_index)
# #             messagebox.showinfo("Dismissed", f"Dismissed Alarm: {dismissed_alarm['time']}")

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = AlarmClock(root)
# #     root.mainloop()
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# import time
# import winsound
# from plyer import notification

# class AlarmClock:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Alarm Clock")
#         self.root.configure(bg="blue")  # Set background color to blue
        
#         self.alarms = []
        
#         self.current_time_label = tk.Label(root, font=("Helvetica", 48), bg="blue", fg="white")
#         self.current_time_label.pack(pady=20)
        
#         self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
#         self.set_alarm_button.pack(pady=10)
        
#         self.alarm_listbox = tk.Listbox(root)
#         self.alarm_listbox.pack(pady=10)
        
#         self.dismiss_button = tk.Button(root, text="Dismiss", command=self.dismiss_alarm)
#         self.dismiss_button.pack(pady=10)
        
#         self.update_time()
#         self.check_alarms()
    
#     def update_time(self):
#         current_time = time.strftime("%H:%M:%S %p")
#         self.current_time_label.config(text=current_time)
#         self.root.after(1000, self.update_time)
    
#     def set_alarm(self):
#         alarm_time = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM AM/PM):")
#         alarm_date = simpledialog.askstring("Set Alarm", "Enter alarm date (MM/DD/YYYY):")
#         if alarm_time and alarm_date:
#             hours, minutes, period = map(str.strip, alarm_time.split(':'))
#             month, day, year = map(str.strip, alarm_date.split('/'))
#             period = period.lower()
#             if period == 'am':
#                 hours = int(hours) % 12
#             else:
#                 hours = (int(hours) % 12) + 12
#             alarm_data = {
#                 "time": f"{month}/{day}/{year} {hours:02d}:{minutes} {period.upper()}",
#                 "active": True  # You can set the alarm as active by default
#             }
#             self.alarms.append(alarm_data)
#             self.alarm_listbox.insert(tk.END, alarm_data["time"])
        
#     def check_alarms(self):
#         current_time = time.strftime("%m/%d/%Y %H:%M %p")
#         for alarm in self.alarms:
#             if alarm["time"] == current_time and alarm["active"]:
#                 winsound.PlaySound("alarm_sound.wav", winsound.SND_FILENAME)
#                 notification_title = "Alarm Notification"
#                 notification_message = f"Alarm: {alarm['time']}"
#                 notification_app_name = "Alarm Clock App"
#                 notification_timeout = 10  # Notification will be visible for 10 seconds
#                 notification.notify(
#                     title=notification_title,
#                     message=notification_message,
#                     app_name=notification_app_name,
#                     timeout=notification_timeout
#                 )
                
#                 response = messagebox.askquestion("Alarm", "Alarm! Snooze?")
#                 if response == 'yes':
#                     # Implement snooze functionality
#                     pass
#                 else:
#                     self.dismiss_alarm()
#         self.root.after(1000, self.check_alarms)
    
#     def dismiss_alarm(self):
#         winsound.PlaySound(None, winsound.SND_PURGE)  # Stop the alarm sound
#         selected_alarm_index = self.alarm_listbox.curselection()
#         if selected_alarm_index:
#             selected_alarm_index = int(selected_alarm_index[0])
#             dismissed_alarm = self.alarms[selected_alarm_index]
#             self.alarms.pop(selected_alarm_index)
#             self.alarm_listbox.delete(selected_alarm_index)
#             messagebox.showinfo("Dismissed", f"Dismissed Alarm: {dismissed_alarm['time']}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AlarmClock(root)
#     root.mainloop()
import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import winsound
from win10toast import ToastNotifier

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.configure(bg="blue")  # Set background color to blue
        
        self.alarms = []
        self.toaster = ToastNotifier()
        
        self.current_time_label = tk.Label(root, font=("Helvetica", 48), bg="blue", fg="white")
        self.current_time_label.pack(pady=20)
        
        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)
        
        self.alarm_listbox = tk.Listbox(root)
        self.alarm_listbox.pack(pady=10)
        
        self.dismiss_button = tk.Button(root, text="Dismiss", command=self.dismiss_alarm)
        self.dismiss_button.pack(pady=10)
        
        self.update_time()
        self.check_alarms()
    
    def update_time(self):
        current_time = time.strftime("%H:%M:%S %p")
        self.current_time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def set_alarm(self):
        alarm_time = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM AM/PM):")
        alarm_date = simpledialog.askstring("Set Alarm", "Enter alarm date (MM/DD/YYYY):")
        if alarm_time and alarm_date:
            hours, minutes, period = map(str.strip, alarm_time.split(':'))
            month, day, year = map(str.strip, alarm_date.split('/'))
            period = period.lower()
            if period == 'am':
                hours = int(hours) % 12
            else:
                hours = (int(hours) % 12) + 12
            alarm_data = {
                "time": f"{month}/{day}/{year} {hours:02d}:{minutes} {period.upper()}",
                "active": True  # You can set the alarm as active by default
            }
            self.alarms.append(alarm_data)
            self.alarm_listbox.insert(tk.END, alarm_data["time"])
        
    def check_alarms(self):
        current_time = time.strftime("%m/%d/%Y %H:%M %p")
        for alarm in self.alarms:
            if alarm["time"] == current_time and alarm["active"]:
                winsound.PlaySound("alarm_sound.wav", winsound.SND_FILENAME)
                self.toaster.show_toast("Alarm Notification", f"Alarm: {alarm['time']}", duration=10)
                
                response = messagebox.askquestion("Alarm", "Alarm! Snooze?")
                if response == 'yes':
                    # Implement snooze functionality
                    pass
                else:
                    self.dismiss_alarm()
        self.root.after(1000, self.check_alarms)
    
    def dismiss_alarm(self):
        winsound.PlaySound(None, winsound.SND_PURGE)  # Stop the alarm sound
        selected_alarm_index = self.alarm_listbox.curselection()
        if selected_alarm_index:
            selected_alarm_index = int(selected_alarm_index[0])
            dismissed_alarm = self.alarms[selected_alarm_index]
            self.alarms.pop(selected_alarm_index)
            self.alarm_listbox.delete(selected_alarm_index)
            messagebox.showinfo("Dismissed", f"Dismissed Alarm: {dismissed_alarm['time']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
