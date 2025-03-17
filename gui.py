import tkinter as tk
from tkinter import ttk
import variable
import os
from rw_json import RWJson

class App:

    def __init__(self, root):
        self.read_write_event_json = RWJson(variable.event_file)
        self.read_event_json = self.read_write_event_json.read_json()

        self.read_write_assistrules_json = RWJson(variable.assistrules_file)
        self.read_assistrules_json = self.read_write_assistrules_json.read_json()

        self.read_write_configuration_file_json = RWJson(variable.configuration_file)
        self.read_configuration_file_json = self.read_write_configuration_file_json.read_json()

        self.read_write_eventrules_file_json = RWJson(variable.eventrules_file)
        self.read_eventrules_file_json = self.read_write_eventrules_file_json.read_json()

        self.read_write_setting_file_json = RWJson(variable.setting_file)
        self.read_setting_file_json = self.read_write_setting_file_json.read_json()

        self.practice_check_var = tk.IntVar()
        self.qualifying_check_var = tk.IntVar()
        self.root = root
        self.root.title("ACC setup GUI")

        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Event Frame
        self.event_frame = tk.LabelFrame(self.main_frame, text="Event")
        self.event_frame.grid(row=0, column=0, padx=0, pady=0)

        tk.Label(self.event_frame, text="Track").grid(row=0, column=0)
        self.track_combobox = ttk.Combobox(self.event_frame, values=list(i for i in variable.tracks))
        self.track_combobox.insert(0, self.read_event_json["track"])
        self.track_combobox.grid(row=0, column=1)

        tk.Label(self.event_frame, text="Pre Race Waiting Time Seconds").grid(row=1, column=0)
        self.preracewaitingtimeseconds_spinbox = tk.Spinbox(self.event_frame, from_=1, to=100,
                                                            )
        self.preracewaitingtimeseconds_spinbox.delete(0, tk.END)
        self.preracewaitingtimeseconds_spinbox.insert(0, self.read_event_json["preRaceWaitingTimeSeconds"])
        self.preracewaitingtimeseconds_spinbox.grid(row=1, column=1)

        tk.Label(self.event_frame, text="Session Over Time Seconds").grid(row=2, column=0)
        self.sessionovertimeseconds_spinbox = tk.Spinbox(self.event_frame, from_=1, to=100,
                                                         )
        self.sessionovertimeseconds_spinbox.delete(0, tk.END)
        self.sessionovertimeseconds_spinbox.insert(0, self.read_event_json["sessionOverTimeSeconds"])
        self.sessionovertimeseconds_spinbox.grid(row=2, column=1)

        tk.Label(self.event_frame, text="Ambient Temp").grid(row=3, column=0)
        self.ambienttemp_spinbox = tk.Spinbox(self.event_frame, from_=1, to=50,
                                              )
        self.ambienttemp_spinbox.delete(0, tk.END)
        self.ambienttemp_spinbox.insert(0, self.read_event_json["ambientTemp"])
        self.ambienttemp_spinbox.grid(row=3, column=1)

        tk.Label(self.event_frame, text="Cloud Level").grid(row=4, column=0)
        self.cloudlevel_spinbox = tk.Spinbox(self.event_frame, from_=0, to=50,
                                             increment=.1)
        self.cloudlevel_spinbox.delete(0, tk.END)
        self.cloudlevel_spinbox.insert(0, self.read_event_json["cloudLevel"])
        self.cloudlevel_spinbox.grid(row=4, column=1)

        tk.Label(self.event_frame, text="Rain").grid(row=5, column=0)
        self.rain_spinbox = tk.Spinbox(self.event_frame, from_=0, to=1,
                                       increment=.1)
        self.rain_spinbox.delete(0, tk.END)
        self.rain_spinbox.insert(0, self.read_event_json["rain"])
        self.rain_spinbox.grid(row=5, column=1)

        tk.Label(self.event_frame, text="Weather Randomness").grid(row=7, column=0)
        self.weatherrandomness_spinbox = tk.Spinbox(self.event_frame, from_=0, to=7)
        self.weatherrandomness_spinbox.delete(0, tk.END)
        self.weatherrandomness_spinbox.insert(0, self.read_event_json["weatherRandomness"])
        self.weatherrandomness_spinbox.grid(row=7, column=1)

        # Practice
        self.practice_session_frame = tk.LabelFrame(self.event_frame, text="Event")
        self.practice_session_frame.grid(row=8, column=0, padx=0, pady=0)

        # self.practice_checkbox = tk.Checkbutton(self.practice_session_frame, text="Practice disables", variable=self.practice_check_var,
        #                                         command=lambda: self.disable_enable(
        #                                             self.practice_session_frame))
        # self.practice_checkbox.grid(row=0, column=0, padx=0, pady=0)

        tk.Label(self.practice_session_frame, text="Hour of Day").grid(row=1, column=0)
        self.practice_hourofday_spinbox = tk.Spinbox(self.practice_session_frame, from_=0, to=23,
                                                     )
        self.practice_hourofday_spinbox.delete(0, tk.END)
        self.practice_hourofday_spinbox.insert(0, self.read_event_json["sessions"][0]["hourOfDay"])
        self.practice_hourofday_spinbox.grid(row=1, column=1)

        tk.Label(self.practice_session_frame, text="Day of Weekend").grid(row=2, column=0)
        self.practice_dayofweekend_spinbox = tk.Spinbox(self.practice_session_frame, from_=0, to=7,
                                                        )
        self.practice_dayofweekend_spinbox.delete(0, tk.END)
        self.practice_dayofweekend_spinbox.insert(0, self.read_event_json["sessions"][0]["dayOfWeekend"])
        self.practice_dayofweekend_spinbox.grid(row=2, column=1)

        tk.Label(self.practice_session_frame, text="Time Multiplier").grid(row=3, column=0)
        self.practice_timemultiplier_spinbox = tk.Spinbox(self.practice_session_frame, from_=0, to=50,
                                                          )
        self.practice_timemultiplier_spinbox.delete(0, tk.END)
        self.practice_timemultiplier_spinbox.insert(0, self.read_event_json["sessions"][0]["timeMultiplier"])
        self.practice_timemultiplier_spinbox.grid(row=3, column=1)

        tk.Label(self.practice_session_frame, text="Session Duration Minutes").grid(row=4, column=0)
        self.practice_sessiondurationminutes_spinbox = tk.Spinbox(self.practice_session_frame, from_=-1, to=50,
                                                                  )
        self.practice_sessiondurationminutes_spinbox.delete(0, tk.END)
        self.practice_sessiondurationminutes_spinbox.insert(0, self.read_event_json["sessions"][0][
            "sessionDurationMinutes"])
        self.practice_sessiondurationminutes_spinbox.grid(row=4, column=1)

        # Qualifying
        self.qualifying_session_frame = tk.LabelFrame(self.event_frame, text="Qualifying")
        self.qualifying_session_frame.grid(row=8, column=1, padx=0, pady=0)

        # self.qualifying_checkbox = tk.Checkbutton(self.qualifying_session_frame, text="Qualifying disables",
        #                                         variable=self.qualifying_check_var,
        #                                         command=lambda: self.disable_enable(
        #                                             self.qualifying_session_frame))
        # self.qualifying_checkbox.grid(row=0, column=0, padx=0, pady=0)

        tk.Label(self.qualifying_session_frame, text="Hour of Day").grid(row=1, column=0)
        self.qualifying_hourofday_spinbox = tk.Spinbox(self.qualifying_session_frame, from_=0, to=23,
                                                       )
        self.qualifying_hourofday_spinbox.delete(0, tk.END)
        self.qualifying_hourofday_spinbox.insert(0, self.read_event_json["sessions"][1]["hourOfDay"])
        self.qualifying_hourofday_spinbox.grid(row=1, column=1)

        tk.Label(self.qualifying_session_frame, text="Day of Weekend").grid(row=2, column=0)
        self.qualifying_dayofweekend_spinbox = tk.Spinbox(self.qualifying_session_frame, from_=0, to=50,
                                                          )
        self.qualifying_dayofweekend_spinbox.delete(0, tk.END)
        self.qualifying_dayofweekend_spinbox.insert(0, self.read_event_json["sessions"][1]["dayOfWeekend"])
        self.qualifying_dayofweekend_spinbox.grid(row=2, column=1)

        tk.Label(self.qualifying_session_frame, text="Time Multiplier").grid(row=3, column=0)
        self.qualifying_timemultiplier_spinbox = tk.Spinbox(self.qualifying_session_frame, from_=0, to=50,
                                                            )
        self.qualifying_timemultiplier_spinbox.delete(0, tk.END)
        self.qualifying_timemultiplier_spinbox.insert(0, self.read_event_json["sessions"][1]["timeMultiplier"])
        self.qualifying_timemultiplier_spinbox.grid(row=3, column=1)

        tk.Label(self.qualifying_session_frame, text="Session Duration Minutes").grid(row=4, column=0)
        self.qualifying_sessiondurationminutes_spinbox = tk.Spinbox(self.qualifying_session_frame, from_=-1, to=50,
                                                                    )
        self.qualifying_sessiondurationminutes_spinbox.delete(0, tk.END)
        self.qualifying_sessiondurationminutes_spinbox.insert(0, self.read_event_json["sessions"][1][
            "sessionDurationMinutes"])
        self.qualifying_sessiondurationminutes_spinbox.grid(row=4, column=1)

        # Race

        self.race_session_frame = tk.LabelFrame(self.event_frame, text="Race")
        self.race_session_frame.grid(row=9, column=0, padx=0, pady=0)

        tk.Label(self.race_session_frame, text="Hour of Day").grid(row=1, column=0)
        self.race_hourofday_spinbox = tk.Spinbox(self.race_session_frame, from_=0, to=23,
                                                 )
        self.race_hourofday_spinbox.delete(0, tk.END)
        self.race_hourofday_spinbox.insert(0, self.read_event_json["sessions"][2]["hourOfDay"])
        self.race_hourofday_spinbox.grid(row=1, column=1)

        tk.Label(self.race_session_frame, text="Day of Weekend").grid(row=2, column=0)
        self.race_dayofweekend_spinbox = tk.Spinbox(self.race_session_frame, from_=0, to=50,
                                                    )
        self.race_dayofweekend_spinbox.delete(0, tk.END)
        self.race_dayofweekend_spinbox.insert(0, self.read_event_json["sessions"][2]["dayOfWeekend"])
        self.race_dayofweekend_spinbox.grid(row=2, column=1)

        tk.Label(self.race_session_frame, text="Time Multiplier").grid(row=3, column=0)
        self.race_timemultiplier_spinbox = tk.Spinbox(self.race_session_frame, from_=0, to=50,
                                                      )
        self.race_timemultiplier_spinbox.delete(0, tk.END)
        self.race_timemultiplier_spinbox.insert(0, self.read_event_json["sessions"][2]["timeMultiplier"])
        self.race_timemultiplier_spinbox.grid(row=3, column=1)

        tk.Label(self.race_session_frame, text="Session Duration Minutes").grid(row=4, column=0)
        self.race_sessiondurationminutes_spinbox = tk.Spinbox(self.race_session_frame, from_=-1, to=50,
                                                              )
        self.race_sessiondurationminutes_spinbox.delete(0, tk.END)
        self.race_sessiondurationminutes_spinbox.insert(0, self.read_event_json["sessions"][2][
            "sessionDurationMinutes"])
        self.race_sessiondurationminutes_spinbox.grid(row=4, column=1)

        # Event Rules Frame
        self.event_rule_frame = tk.LabelFrame(self.main_frame, text="Event Rules")
        self.event_rule_frame.grid(row=0, column=1, padx=0, pady=0)
        tk.Label(self.event_rule_frame, text="qualifyStandingType").grid(row=0, column=0)

        tk.Label(self.event_rule_frame, text="Qualify Standing Type").grid(row=0, column=0)
        self.qualifystandingtype_spinbox = tk.Spinbox(self.event_rule_frame, from_=1, to=2)
        self.qualifystandingtype_spinbox.delete(0, tk.END)
        self.qualifystandingtype_spinbox.insert(0, self.read_eventrules_file_json["qualifyStandingType"])
        self.qualifystandingtype_spinbox.grid(row=0, column=1)

        tk.Label(self.event_rule_frame, text="Pit Window Length Sec").grid(row=1, column=0)
        self.pitWindowlengthsec_spinbox = tk.Spinbox(self.event_rule_frame, from_=-1, to=600)
        self.pitWindowlengthsec_spinbox.delete(0, tk.END)
        self.pitWindowlengthsec_spinbox.insert(0, self.read_eventrules_file_json["pitWindowLengthSec"])
        self.pitWindowlengthsec_spinbox.grid(row=1, column=1)

        tk.Label(self.event_rule_frame, text="Driver Stint Time Sec").grid(row=2, column=0)
        self.driverstinttimesec_spinbox = tk.Spinbox(self.event_rule_frame, from_=-1, to=50)
        self.driverstinttimesec_spinbox.delete(0, tk.END)
        self.driverstinttimesec_spinbox.insert(0, self.read_eventrules_file_json["driverStintTimeSec"])
        self.driverstinttimesec_spinbox.grid(row=2, column=1)

        tk.Label(self.event_rule_frame, text="Mandatory Pitstop Count").grid(row=3, column=0)
        self.mandatorypitstopcount_spinbox = tk.Spinbox(self.event_rule_frame, from_=0, to=50)
        self.mandatorypitstopcount_spinbox.delete(0, tk.END)
        self.mandatorypitstopcount_spinbox.insert(0, self.read_eventrules_file_json["mandatoryPitstopCount"])
        self.mandatorypitstopcount_spinbox.grid(row=3, column=1)

        tk.Label(self.event_rule_frame, text="Max Total Driving Time").grid(row=4, column=0)
        self.maxtotaldrivingtime_spinbox = tk.Spinbox(self.event_rule_frame, from_=-1, to=50)
        self.maxtotaldrivingtime_spinbox.delete(0, tk.END)
        self.maxtotaldrivingtime_spinbox.insert(0, self.read_eventrules_file_json["maxTotalDrivingTime"])
        self.maxtotaldrivingtime_spinbox.grid(row=4, column=1)

        tk.Label(self.event_rule_frame, text="Max Drivers Count").grid(row=5, column=0)
        self.maxdriverscount_spinbox = tk.Spinbox(self.event_rule_frame, from_=1, to=4)
        self.maxdriverscount_spinbox.delete(0, tk.END)
        self.maxdriverscount_spinbox.insert(0, self.read_eventrules_file_json["maxDriversCount"])
        self.maxdriverscount_spinbox.grid(row=5, column=1)

        tk.Label(self.event_rule_frame, text="Tyre Set Count").grid(row=6, column=0)
        self.tyresetcount_spinbox = tk.Spinbox(self.event_rule_frame, from_=1, to=50)
        self.tyresetcount_spinbox.delete(0, tk.END)
        self.tyresetcount_spinbox.insert(0, self.read_eventrules_file_json["tyreSetCount"])
        self.tyresetcount_spinbox.grid(row=6, column=1)

        tk.Label(self.event_rule_frame, text="Is Refuelling Allowed In Race").grid(row=7, column=0)
        self.isrefuellingallowedInrace_combobox = ttk.Combobox(self.event_rule_frame,
                                                               values=list(i.lower() for i in variable.bool_exp))
        self.isrefuellingallowedInrace_combobox.insert(0,
                                                       str(self.read_eventrules_file_json[
                                                               "isRefuellingAllowedInRace"]).lower())
        self.isrefuellingallowedInrace_combobox.grid(row=7, column=1)

        tk.Label(self.event_rule_frame, text="Is Refuelling Time Fixed").grid(row=8, column=0)
        self.isrefuellingtimefixed_combobox = ttk.Combobox(self.event_rule_frame,
                                                           values=list(i.lower() for i in variable.bool_exp))
        self.isrefuellingtimefixed_combobox.insert(0,
                                                   str(self.read_eventrules_file_json["isRefuellingTimeFixed"]).lower())
        self.isrefuellingtimefixed_combobox.grid(row=8, column=1)

        tk.Label(self.event_rule_frame, text="Is Mandatory Pitstop Refuelling Required").grid(row=9, column=0)
        self.ismandatorypitstoprefuellingrequired_combobox = ttk.Combobox(self.event_rule_frame,
                                                                          values=list(
                                                                              i.lower() for i in variable.bool_exp))
        self.ismandatorypitstoprefuellingrequired_combobox.insert(0,
                                                                  str(self.read_eventrules_file_json[
                                                                          "isMandatoryPitstopRefuellingRequired"]).lower())
        self.ismandatorypitstoprefuellingrequired_combobox.grid(row=9, column=1)

        tk.Label(self.event_rule_frame, text="Is Mandatory Pitstop Tyre Change Required").grid(row=10, column=0)
        self.ismandatorypitstoptyrechangerequired_combobox = ttk.Combobox(self.event_rule_frame,
                                                                          values=list(
                                                                              i for i in variable.bool_exp))
        self.ismandatorypitstoptyrechangerequired_combobox.insert(0,
                                                                  str(self.read_eventrules_file_json[
                                                                          "isMandatoryPitstopTyreChangeRequired"]).lower())
        self.ismandatorypitstoptyrechangerequired_combobox.grid(row=10, column=1)

        tk.Label(self.event_rule_frame, text="Is Mandatory Pitstop Swap Driver Required").grid(row=11, column=0)
        self.ismandatorypitstopswapdriverrequired_combobox = ttk.Combobox(self.event_rule_frame,
                                                                          values=list(
                                                                              i for i in variable.bool_exp))
        self.ismandatorypitstopswapdriverrequired_combobox.insert(0,
                                                                  str(self.read_eventrules_file_json[
                                                                          "isMandatoryPitstopSwapDriverRequired"]).lower())
        self.ismandatorypitstopswapdriverrequired_combobox.grid(row=11, column=1)

        # Setting Frame
        self.setting_frame = tk.LabelFrame(self.main_frame, text="Setting")
        self.setting_frame.grid(row=1, column=0, padx=0, pady=0)

        tk.Label(self.setting_frame, text="Server Name").grid(row=0, column=0)
        self.servername_entry = tk.Entry(self.setting_frame)
        self.servername_entry.delete(0, tk.END)
        self.servername_entry.insert(0, self.read_setting_file_json["serverName"])
        self.servername_entry.grid(row=0, column=1)

        tk.Label(self.setting_frame, text="Admin Password").grid(row=1, column=0)
        self.adminpassword_entry = tk.Entry(self.setting_frame)
        self.adminpassword_entry.delete(0, tk.END)
        self.adminpassword_entry.insert(0, self.read_setting_file_json["adminPassword"])
        self.adminpassword_entry.grid(row=1, column=1)

        tk.Label(self.setting_frame, text="Car Group").grid(row=2, column=0)
        self.cargroup_combobox = ttk.Combobox(self.setting_frame,
                                              values=list(i for i in variable.car_group))
        self.cargroup_combobox.insert(0, self.read_setting_file_json["carGroup"])
        self.cargroup_combobox.grid(row=2, column=1)

        tk.Label(self.setting_frame, text="Track Medals Requirement").grid(row=3, column=0)
        self.trackmedalsrequirement_spinbox = tk.Spinbox(self.setting_frame, from_=-1, to=4)
        self.trackmedalsrequirement_spinbox.delete(0, tk.END)
        self.trackmedalsrequirement_spinbox.insert(0, self.read_setting_file_json["trackMedalsRequirement"])
        self.trackmedalsrequirement_spinbox.grid(row=3, column=1)

        tk.Label(self.setting_frame, text="Safety Rating Requirement").grid(row=4, column=0)
        self.safetyratingrequirement_spinbox = tk.Spinbox(self.setting_frame, from_=-1, to=4)
        self.safetyratingrequirement_spinbox.delete(0, tk.END)
        self.safetyratingrequirement_spinbox.insert(0, self.read_setting_file_json["safetyRatingRequirement"])
        self.safetyratingrequirement_spinbox.grid(row=4, column=1)

        tk.Label(self.setting_frame, text="Racecraft Rating Requirement").grid(row=5, column=0)
        self.racecraftRatingRequirement_spinbox = tk.Spinbox(self.setting_frame, from_=-1, to=4)
        self.racecraftRatingRequirement_spinbox.delete(0, tk.END)
        self.racecraftRatingRequirement_spinbox.insert(0, self.read_setting_file_json["racecraftRatingRequirement"])
        self.racecraftRatingRequirement_spinbox.grid(row=5, column=1)

        tk.Label(self.setting_frame, text="Password").grid(row=6, column=0)
        self.password_entry = tk.Entry(self.setting_frame)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, self.read_setting_file_json["password"])
        self.password_entry.grid(row=6, column=1)

        tk.Label(self.setting_frame, text="Max Car Slots").grid(row=7, column=0)
        self.maxcarslots_spinbox = tk.Spinbox(self.setting_frame, from_=-1, to=4)
        self.maxcarslots_spinbox.delete(0, tk.END)
        self.maxcarslots_spinbox.insert(0, self.read_setting_file_json["maxCarSlots"])
        self.maxcarslots_spinbox.grid(row=7, column=1)

        tk.Label(self.setting_frame, text="Spectator Password").grid(row=8, column=0)
        self.spectatorpassword_entry = tk.Entry(self.setting_frame)
        self.spectatorpassword_entry.delete(0, tk.END)
        self.spectatorpassword_entry.insert(0, self.read_setting_file_json["spectatorPassword"])
        self.spectatorpassword_entry.grid(row=8, column=1)

        # Assist Rule Frame
        self.assist_rule_frame = tk.LabelFrame(self.main_frame, text="Assist Rule")
        self.assist_rule_frame.grid(row=1, column=1, padx=0, pady=0)
        tk.Label(self.assist_rule_frame, text="disableIdealLine").grid(row=0, column=0)

        tk.Label(self.assist_rule_frame, text="Disable Ideal Line").grid(row=0, column=0)
        self.disableidealline_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableidealline_spinbox.delete(0, tk.END)
        self.disableidealline_spinbox.insert(0, self.read_assistrules_json["disableIdealLine"])
        self.disableidealline_spinbox.grid(row=0, column=1)

        tk.Label(self.assist_rule_frame, text="Disable Auto steer").grid(row=1, column=0)
        self.disableautosteer_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautosteer_spinbox.delete(0, tk.END)
        self.disableautosteer_spinbox.insert(0, self.read_assistrules_json["disableAutosteer"])
        self.disableautosteer_spinbox.grid(row=1, column=1)

        tk.Label(self.assist_rule_frame, text="Stability Control Level Max").grid(row=2, column=0)
        self.stabilitycontrollevelmax_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=100)
        self.stabilitycontrollevelmax_spinbox.delete(0, tk.END)
        self.stabilitycontrollevelmax_spinbox.insert(0, self.read_assistrules_json["stabilityControlLevelMax"])
        self.stabilitycontrollevelmax_spinbox.grid(row=2, column=1)

        tk.Label(self.assist_rule_frame, text="Disable AutoPit Limiter").grid(row=3, column=0)
        self.disableautopitlimiter_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautopitlimiter_spinbox.delete(0, tk.END)
        self.disableautopitlimiter_spinbox.insert(0, self.read_assistrules_json["disableAutoPitLimiter"])
        self.disableautopitlimiter_spinbox.grid(row=3, column=1)

        tk.Label(self.assist_rule_frame, text="Disable Auto Gear").grid(row=4, column=0)
        self.disableautogear_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautogear_spinbox.delete(0, tk.END)
        self.disableautogear_spinbox.insert(0, self.read_assistrules_json["disableAutoGear"])
        self.disableautogear_spinbox.grid(row=4, column=1)

        tk.Label(self.assist_rule_frame, text="Disable Auto Clutch").grid(row=5, column=0)
        self.disableautoclutch_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautoclutch_spinbox.delete(0, tk.END)
        self.disableautoclutch_spinbox.insert(0, self.read_assistrules_json["disableAutoClutch"])
        self.disableautoclutch_spinbox.grid(row=5, column=1)

        tk.Label(self.assist_rule_frame, text="Disable Auto Engine Start").grid(row=6, column=0)
        self.disableautoenginestart_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautoenginestart_spinbox.delete(0, tk.END)
        self.disableautoenginestart_spinbox.insert(0, self.read_assistrules_json["disableAutoEngineStart"])
        self.disableautoenginestart_spinbox.grid(row=6, column=1)

        tk.Label(self.assist_rule_frame, text="Disable Auto Wiper").grid(row=7, column=0)
        self.disableautowiper_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautowiper_spinbox.delete(0, tk.END)
        self.disableautowiper_spinbox.insert(0, self.read_assistrules_json["disableAutoWiper"])
        self.disableautowiper_spinbox.grid(row=7, column=1)

        tk.Label(self.assist_rule_frame, text="Disable Auto Lights").grid(row=8, column=0)
        self.disableautolights_spinbox = tk.Spinbox(self.assist_rule_frame, from_=0, to=1)
        self.disableautolights_spinbox.delete(0, tk.END)
        self.disableautolights_spinbox.insert(0, self.read_assistrules_json["disableAutoLights"])
        self.disableautolights_spinbox.grid(row=8, column=1)

        # Config Frame
        self.config_frame = tk.LabelFrame(self.main_frame, text="Config")
        self.config_frame.grid(row=2, column=0, padx=0, pady=0)

        tk.Label(self.config_frame, text="UDP Port").grid(row=0, column=0)
        self.udpPort_entry = tk.Entry(self.config_frame)
        self.udpPort_entry.delete(0, tk.END)
        self.udpPort_entry.insert(0, self.read_configuration_file_json["udpPort"])
        self.udpPort_entry.config(state='disabled')
        self.udpPort_entry.grid(row=0, column=1)

        tk.Label(self.config_frame, text="TCP Port").grid(row=1, column=0)
        self.tcpPort_entry = tk.Entry(self.config_frame)
        self.tcpPort_entry.delete(0, tk.END)
        self.tcpPort_entry.insert(0, self.read_configuration_file_json["tcpPort"])
        self.tcpPort_entry.config(state='disabled')
        self.tcpPort_entry.grid(row=1, column=1)

        tk.Label(self.config_frame, text="Max Connections").grid(row=2, column=0)
        self.maxConnections_entry = tk.Entry(self.config_frame)
        self.maxConnections_entry.delete(0, tk.END)
        self.maxConnections_entry.insert(0, self.read_configuration_file_json["maxConnections"])
        self.maxConnections_entry.config(state='disabled')
        self.maxConnections_entry.grid(row=2, column=1)

        # Buttons
        self.botton_frame = tk.LabelFrame(self.main_frame, text="")
        self.botton_frame.grid(row=3, column=0, padx=0, pady=0)

        tk.Button(self.botton_frame, text="Reset", command=self.reset).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.botton_frame, text="Apply", command=self.write).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.botton_frame, text="Start Server", command=self.start_program).grid(row=3, column=2, padx=10,
                                                                                           pady=10)

    def reset(self):
        self.track_combobox.update()
        print(self.cargroup_combobox.get())

    def write(self):
        # if self.practice_check_var.get() == 1:
        #     self.read_write_event_json.delete("sessions", 0)
        # elif self.practice_check_var.get() == 0:
        #     self.read_write_event_json.write_json("hourOfDay", self.practice_hourofday_spinbox.get(),  0)
        #     self.read_write_event_json.write_json("dayOfWeekend", self.practice_dayofweekend_spinbox.get(), 0)
        #     self.read_write_event_json.write_json("timeMultiplier", self.practice_timemultiplier_spinbox.get(), 0)
        #     self.read_write_event_json.write_json("sessionType", "sessionType")
        #     self.read_write_event_json.write_json("sessionDurationMinutes", self.practice_sessiondurationminutes_spinbox.get(), 0)

        #####################################################################
        # Config file
        #####################################################################
        self.read_write_event_json.write_json("track", self.track_combobox.get())
        self.read_write_event_json.write_json("preRaceWaitingTimeSeconds", int(self.preracewaitingtimeseconds_spinbox.get()))
        self.read_write_event_json.write_json("sessionOverTimeSeconds", int(self.sessionovertimeseconds_spinbox.get()))
        self.read_write_event_json.write_json("ambientTemp", int(self.ambienttemp_spinbox.get()))
        self.read_write_event_json.write_json("cloudLevel", float(self.cloudlevel_spinbox.get()))
        self.read_write_event_json.write_json("rain", float(self.rain_spinbox.get()))
        self.read_write_event_json.write_json("weatherRandomness", int(self.weatherrandomness_spinbox.get()))

        # Practice
        self.read_write_event_json.write_json("hourOfDay",int(self.practice_hourofday_spinbox.get()), 0)
        self.read_write_event_json.write_json("dayOfWeekend", int(self.practice_dayofweekend_spinbox.get()), 0)
        self.read_write_event_json.write_json("timeMultiplier", int(self.practice_timemultiplier_spinbox.get()), 0)
        self.read_write_event_json.write_json("sessionDurationMinutes",
                                              int(self.practice_sessiondurationminutes_spinbox.get()), 0)

        # Qualifying
        self.read_write_event_json.write_json("hourOfDay", int(self.qualifying_hourofday_spinbox.get()), 1)
        self.read_write_event_json.write_json("dayOfWeekend", int(self.qualifying_dayofweekend_spinbox.get()), 1)
        self.read_write_event_json.write_json("timeMultiplier", int(self.qualifying_timemultiplier_spinbox.get()), 1)
        self.read_write_event_json.write_json("sessionDurationMinutes",
                                              int(self.qualifying_sessiondurationminutes_spinbox.get()), 1)

        # Race
        self.read_write_event_json.write_json("hourOfDay", int(self.race_hourofday_spinbox.get()), 2)
        self.read_write_event_json.write_json("dayOfWeekend", int(self.race_dayofweekend_spinbox.get()), 2)
        self.read_write_event_json.write_json("timeMultiplier", int(self.race_timemultiplier_spinbox.get()), 2)
        self.read_write_event_json.write_json("sessionDurationMinutes",
                                              int(self.race_sessiondurationminutes_spinbox.get()), 2)

        #####################################################################
        # Event Rules file
        #####################################################################
        self.read_write_eventrules_file_json.write_json("qualifyStandingType", int(self.qualifystandingtype_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("pitWindowLengthSec", int(self.pitWindowlengthsec_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("driverStintTimeSec", int(self.driverstinttimesec_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("mandatoryPitstopCount",
                                                        int(self.mandatorypitstopcount_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("maxTotalDrivingTime", int(self.maxtotaldrivingtime_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("maxDriversCount", int(self.maxdriverscount_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("maxDriversCount", int(self.tyresetcount_spinbox.get()))
        self.read_write_eventrules_file_json.write_json("isRefuellingAllowedInRace",
                                                        self.isrefuellingallowedInrace_combobox.get())
        self.read_write_eventrules_file_json.write_json("isRefuellingTimeFixed",
                                                        self.isrefuellingtimefixed_combobox.get())
        self.read_write_eventrules_file_json.write_json("isMandatoryPitstopRefuellingRequired",
                                                        self.ismandatorypitstoprefuellingrequired_combobox.get())
        self.read_write_eventrules_file_json.write_json("isMandatoryPitstopTyreChangeRequired",
                                                        self.ismandatorypitstoptyrechangerequired_combobox.get())
        self.read_write_eventrules_file_json.write_json("isMandatoryPitstopSwapDriverRequired",
                                                        self.ismandatorypitstopswapdriverrequired_combobox.get())

        #####################################################################
        # Setting file
        #####################################################################

        self.read_write_setting_file_json.write_json("serverName", self.servername_entry.get())
        self.read_write_setting_file_json.write_json("adminPassword", self.adminpassword_entry.get())
        self.read_write_setting_file_json.write_json("carGroup", self.cargroup_combobox.get())
        self.read_write_setting_file_json.write_json("trackMedalsRequirement",
                                                     int(self.trackmedalsrequirement_spinbox.get()))
        self.read_write_setting_file_json.write_json("safetyRatingRequirement",
                                                     int(self.safetyratingrequirement_spinbox.get()))
        self.read_write_setting_file_json.write_json("racecraftRatingRequirement",
                                                     int(self.racecraftRatingRequirement_spinbox.get()))
        self.read_write_setting_file_json.write_json("password", self.password_entry.get())
        self.read_write_setting_file_json.write_json("maxCarSlots", int(self.maxcarslots_spinbox.get()))
        self.read_write_setting_file_json.write_json("spectatorPassword", self.spectatorpassword_entry.get())

        #####################################################################
        # Assist Rule file
        #####################################################################
        self.read_write_assistrules_json.write_json("disableIdealLine", int(self.disableidealline_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutosteer", int(self.disableautosteer_spinbox.get()))
        self.read_write_assistrules_json.write_json("stabilityControlLevelMax", int(self.stabilitycontrollevelmax_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutoPitLimiter", int(self.disableautopitlimiter_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutoGear", int(self.disableautogear_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutoClutch", int(self.disableautoclutch_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutoEngineStart", int(self.disableautoenginestart_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutoWiper", int(self.disableautowiper_spinbox.get()))
        self.read_write_assistrules_json.write_json("disableAutoLights", int(self.disableautolights_spinbox.get()))

        #####################################################################
        # Config file
        #####################################################################

    # def disable_enable(self, frame):
    #     print(self.practice_check_var.get())
    #     if (self.practice_check_var.get() or self.qualifying_check_var.get()) == 1:
    #         for child in frame.winfo_children():
    #             if child.winfo_class() == 'Spinbox':
    #                 child.config(state='disabled')
    #     elif (self.practice_check_var.get() or self.qualifying_check_var.get()) == 0:
    #         print("enable")
    #         for child in frame.winfo_children():
    #             if child.winfo_class() == 'Spinbox':
    #                 child.config(state='normal')

    def start_program(self):
        os.startfile(variable.start_file)