from pyModbusTCP.client import ModbusClient
import time
temp_ulica = 0
num = [10]
dis_in_regs = []
in_regs_read = []
hl_regs_read = []
coil_regs_read = []
CL_POWER = []  # r/w Увімк./вимк. установку
CL_TIMER = []  # r/w Основний таймер
CL_WEEK = []  # r Тижневий розклад
CL_Boost_MODE = []  # r Режим Boost
CL_FPLC_MODE = []  # r/w Режим Камін
CL_IntRH_CTRL = []  # r/w Активація основного датчика вологост
CL_ExtRH_CTRL = []  # r/w Активація зовнішнього датчика вологості
CL_IntCO2_CTRL = []  # r/w Активація основного датчика CO2
CL_ExtCO2_CTRL = []  # r/w Активація зовнішнього датчика CO2
CL_IntPM2_5_CTRL = []  # r/w Активація основного датчика PM2,5
CL_ExtPM2_5_CTRL = []  # r/w Активація зовнішнього датчика PM2,5
CL_IntVOC_CTRL = []  # r/w r/w Активація основного датчика VOC
CL_ExtVOC_CTRL = []  # r/w Активація зовнішнього датчика VOC
CL_BoostSWITCH_CTRL = []  # Активація входу для вимикача режиму Boost
CL_FplcSWITCH_CTRL = []  # r/w Активація входу для вимикача режиму Камін
CL_FireALARM_CTRL = []  # r/w Активація датчика пожежної сигналізації
CL_10V_SENSOR_CTRL = []  # r/w Активація входу для зовнішнього пристрою керування 0-10 В
CL_RESET_FILTER_TIMER = []  # w  Скинути час зворотного відліку таймера до заміни фільтра
CL_RESET_ALARM = []  # w Скинути усі аварії
CL_RESTORE_FACTORY = []  # w Відновити усе до заводських налаштувань
CL_CLOUD_CTRL = []  # r/w Активація керування через хмарний сервер
CL_MinSuAirOutTEMP_CTRL = []  # r/w  Конт. мін. темп. припл. пов. у прим.
CL_WaterPRESS_CTRL = []  # r/w Активація датчика тиску води теплоносія
CL_WaterFLOW_CTRL = []  # r/w Активація датчика протоку води теплоносія
CL_WaterHeaterAutoRestart = []  # r/w Акт. функції авт. перез. ПВУ в разі падін. темп. звор.>ав
IR_CurSelTEMP = []
IR_CurTEMP_SuAirIn = []
host_client = "192.168.1.220"
c = ModbusClient()
if not c.host(host_client):
    print("host error")
if not c.port(502):
    print("port error")

# TCP auto connect on modbus request, close after it
c = ModbusClient(host=host_client, auto_open=True, auto_close=True)

while True:
    if c.is_open():
        in_regs_read = c.read_input_registers(0, 50)
        hl_regs_read = c.read_holding_registers(0, 100)
        coil_regs_read = c.read_coils(0, 24)
        dis_in_regs = c.read_discrete_inputs(0, 71)
# ''' coil'''
        CL_POWER = coil_regs_read[0:1]  # r/w Увімк./вимк. установку
        CL_TIMER = coil_regs_read[1:2]  # r/w Основний таймер
        CL_WEEK = coil_regs_read[2:3]  # r Тижневий розклад
        CL_Boost_MODE = coil_regs_read[3:4]  # r Режим Boost
        CL_FPLC_MODE = coil_regs_read[4:5]  # r/w Режим Камін
        CL_IntRH_CTRL = coil_regs_read[5:6]  # r/w Активація основного датчика вологост
        CL_ExtRH_CTRL = coil_regs_read[6:7]  # r/w Активація зовнішнього датчика вологості
        CL_IntCO2_CTRL = coil_regs_read[7:8]  # r/w Активація основного датчика CO2
        CL_ExtCO2_CTRL = coil_regs_read[8:9]  # r/w Активація зовнішнього датчика CO2
        CL_IntPM2_5_CTRL = coil_regs_read[9:10]  # r/w Активація основного датчика PM2,5
        CL_ExtPM2_5_CTRL = coil_regs_read[10:11]  # r/w Активація зовнішнього датчика PM2,5
        CL_IntVOC_CTRL = coil_regs_read[11:12]  # r/w r/w Активація основного датчика VOC
        CL_ExtVOC_CTRL = coil_regs_read[12:13]  # r/w Активація зовнішнього датчика VOC
        CL_BoostSWITCH_CTRL = coil_regs_read[13:14]  # Активація входу для вимикача режиму Boost
        CL_FplcSWITCH_CTRL = coil_regs_read[14:15]  # r/w Активація входу для вимикача режиму Камін
        CL_FireALARM_CTRL = coil_regs_read[15:16]  # r/w Активація датчика пожежної сигналізації
        CL_10V_SENSOR_CTRL = coil_regs_read[16:17]  # r/w Активація входу для зовнішнього пристрою керування 0-10 В
        CL_RESET_FILTER_TIMER = coil_regs_read[17:18]  # w  Скинути час зворотного відліку таймера до заміни фільтра
        CL_RESET_ALARM = coil_regs_read[18:19]  # w Скинути усі аварії
        CL_RESTORE_FACTORY = coil_regs_read[19:20]  # w Відновити усе до заводських налаштувань
        CL_CLOUD_CTRL = coil_regs_read[20:21]  # r/w Активація керування через хмарний сервер
        CL_MinSuAirOutTEMP_CTRL = coil_regs_read[21:22]  # r/w  Конт. мін. темп. припл. пов. у прим.
        CL_WaterPRESS_CTRL = coil_regs_read[22:23]  # r/w Активація датчика тиску води теплоносія
        CL_WaterFLOW_CTRL = coil_regs_read[23:24]  # r/w Активація датчика протоку води теплоносія
        CL_WaterHeaterAutoRestart = coil_regs_read[23:25]  #  r/w Акт. функції авт. перез. ПВУ в разі падін. темп. звор.>ав
#   '''Input Registers '''

        IR_CurSelTEMP = in_regs_read[0:1]  # R Поточна температура обраного датчика
        IR_CurTEMP_SuAirIn = in_regs_read[1:2]  # R Поточна температура основного датчика вуличного повітря
        IR_CurTEMP_SuAirOut = in_regs_read[2:3]  # R Поточна температура основного датчика припливного повітря на виході
        IR_CurTEMP_ExAirIn = in_regs_read[3:4]  # R Поточна температура витяжного повітря на вході в установку
        IR_CurTEMP_ExAirOut = in_regs_read[4:5]  # R Поточна температура витяжного повітря на виході з установки
        IR_CurTEMP_Ext = in_regs_read[5:6]  # R Поточна температура зовнішнього датчика температури (у панелі керування, .
        IR_CurTEMP_Water = in_regs_read[8:9]  # R Температура зворотного теплоносія
        IR_CurVBAT = in_regs_read[9:10]  # R Поточна напруга батарейки для RTC.
        IR_CurRH_Int = in_regs_read[10:11]  # R Поточна вологість основного датчика.
        IR_CurRH_Ext = in_regs_read[11:12]  # R Поточна вологість зовнішнього датчика.
        IR_CurCO2_Int = in_regs_read[12:13]  # R Поточний рівень СО2 основного датчика.
        IR_CurCO2_Ext = in_regs_read[13:14]  # R Поточний рівень СО2 основного датчика.
        IR_CurPM2_5_Int = in_regs_read[14:15]  # R Поточний рівень РМ2,5 основного датчика.
        IR_CurPM2_5_Ext = in_regs_read[15:16]  # R Поточний рівень РМ2,5 зовнішнього датчика.
        IR_CurVOC_Int = in_regs_read[16:17]  # R Поточний рівень VOC основного датчика.
        IR_CurVOC_Ext = in_regs_read[17:18]  # R Поточний рівень VOC зовнішнього датчика.
        IR_Cur10V_SENSOR = in_regs_read[18:19]  # R Поточний рівень датчика 0-10 В
        IR_CurSuAirFLOW = in_regs_read[19:20]  # R
        IR_CurExAirFLOW = in_regs_read[20:21]  # R
        IR_CurSuPRESS = in_regs_read[21:22]  # R
        IR_CurExPRESS = in_regs_read[22:23]  # R
        IR_SuRPM = in_regs_read[23:24]  # R
        IR_ExRPM = in_regs_read[24:25]  # R
        IR_CurTIMER_TIME = in_regs_read[25:26]  # R
        IR_CurFILTER_TIMER = in_regs_read[26:27]  # R
        IR_TotalWorkingTime = in_regs_read[29:30]  # R
        IR_StateFILTER = in_regs_read[31:32]  # R
        IR_CurWeekSpeed = in_regs_read[32:33]  # R
        IR_CurWeekSetTemp = in_regs_read[33:34]  # R
        IR_VerMAIN_FMW = in_regs_read[34:35]  # R
        IR_DeviceTYPE = in_regs_read[37:38]  # R
        IR_ALARM = in_regs_read[38:39]  # R
        IR_RH_U = in_regs_read[39:40]  # R
        IR_CO2_U = in_regs_read[40:41]  # R
        IR_PM2_5_U = in_regs_read[41:42]  # R
        IR_VOC_U = in_regs_read[42:43]  # R
        IR_PreHeater_U = in_regs_read[43:44]  # R
        IR_MainHeater_U = in_regs_read[44:45]  # R
        IR_BPS_ROTOR_U = in_regs_read[45:46]  # R
        IR_KKB_U = in_regs_read[46:47]  # R
        IR_ReturnWater_U = in_regs_read[47:48]  # R
        IR_SuAirOutSetTemp = in_regs_read[48:49]  # R
        IR_WaterStandbySetTemp = in_regs_read[49:50]  # R
        IR_WaterStartSetTemp = in_regs_read[50:51]  # R
    else:
        c.open()
        time.sleep(2)
        print("input registers", in_regs_read[0:1])
        print("holding registers ", hl_regs_read[0:1])
        print("coil registers ", coil_regs_read[0:1])
        print("discrete input register", dis_in_regs[6:7])
        print("Температура улица", list(map(lambda x: x / 10, IR_CurTEMP_SuAirIn)))
        print("T", IR_CurTEMP_SuAirIn)
        IR_CurTEMP_SuAirIn = list(map(int, IR_CurTEMP_SuAirIn))
        temp_ulica = (list(map(lambda x: x / 10, IR_CurTEMP_SuAirIn)))
        if temp_ulica > [55]:
            temp_ulica = list(map(lambda x: (65535 - x + 1) / 10, IR_CurTEMP_SuAirIn))
            print("Температура улица минус", "-", temp_ulica)
