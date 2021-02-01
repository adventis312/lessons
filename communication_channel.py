from pyModbusTCP.client import ModbusClient
import time
dis_in_regs = []
in_regs_read = []
hl_regs_read = []
coil_regs_read = []
other = []
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
#
IR_CurSelTEMP = []    # R Поточна температура обраного датчика
IR_CurTEMP_SuAirIn = []  # R Поточна температура основного датчика вуличного повітря
IR_CurTEMP_SuAirOut = []  # R Поточна температура основного датчика припливного повітря на виході
IR_CurTEMP_ExAirIn = []     # R Поточна температура витяжного повітря на вході в установку
IR_CurTEMP_ExAirOut = []  # R Поточна температура витяжного повітря на виході з установки
IR_CurTEMP_Ext = []  # R Поточна температура зовнішнього датчика температури (у панелі керування, .
IR_CurTEMP_Water = []  # R Температура зворотного теплоносія
IR_CurVBAT = []  # R Поточна напруга батарейки для RTC.
IR_CurRH_Int = []     # R Поточна вологість основного датчика.
IR_CurRH_Ext = []     # R Поточна вологість зовнішнього датчика.
IR_CurCO2_Int = []   # R Поточний рівень СО2 основного датчика.
IR_CurCO2_Ext = []  # R Поточний рівень СО2 основного датчика.
IR_CurPM2_5_Int = []  # R Поточний рівень РМ2,5 основного датчика.
IR_CurPM2_5_Ext = []  # R Поточний рівень РМ2,5 зовнішнього датчика.
IR_CurVOC_Int = []   # R Поточний рівень VOC основного датчика.
IR_CurVOC_Ext = []  # R Поточний рівень VOC зовнішнього датчика.
IR_Cur10V_SENSOR = []  # R Поточний рівень датчика 0-10 В
IR_CurSuAirFLOW = []     # R
IR_CurExAirFLOW = []  # R
IR_CurSuPRESS = []  # R
IR_CurExPRESS = []  # R
IR_SuRPM = []  # R
IR_ExRPM = []  # R
IR_CurTIMER_TIME = []  # R
IR_CurFILTER_TIMER = []  # R
IR_TotalWorkingTime = []  # R
IR_StateFILTER = []  # R
IR_CurWeekSpeed = []  # R
IR_CurWeekSetTemp = []  # R
IR_VerMAIN_FMW = []  # R
IR_DeviceTYPE = []  # R
IR_ALARM = []  # R
IR_RH_U = []  # R
IR_CO2_U = []  # R
IR_PM2_5_U = []  # R
IR_VOC_U = []  # R
IR_PreHeater_U = []  # R
IR_MainHeater_U = []  # R
IR_BPS_ROTOR_U = []  # R
IR_KKB_U = []  # R
IR_ReturnWater_U = []  # R
IR_SuAirOutSetTemp = []  # R
IR_WaterStandbySetTemp = []  # R
IR_WaterStartSetTemp = []
unknown6in = []
unknown7in = []
unknown26in = []
unknown28in = []
unknown30in = []
unknown35in = []
unknown36in = []
#
DI_CurBoostSWITCH = []
DI_CurFplcSWITCH = []
DI_CurFireALARM = []
DI_StatusRH = []
DI_StatusCO2 = []
DI_StatusPM2_5 = []
DI_StatusVOC = []
DI_StatusHEATER = []
DI_StatusCOOLER = []
DI_StatusFanBLOWING = []
DI_CurPreHeaterThermostat = []
DI_CurMainHeaterThermostat = []
DI_CurSuFilterPRESS = []
DI_CurExFilterPRESS = []
DI_CurWaterPRESS = []
DI_CurWaterFLOW = []
DI_CurSuFanPRESS = []
DI_CurExFanPRESS = []
DI_WaterPreheatingStatus = []
DI_AlarmCODE0 = []
DI_AlarmCODE1 = []
DI_AlarmCODE2 = []
DI_AlarmCODE3 = []
DI_AlarmCODE4 = []
DI_AlarmCODE5 = []
DI_AlarmCODE6 = []
DI_AlarmCODE7 = []
DI_AlarmCODE8 = []
DI_AlarmCODE9 = []
DI_AlarmCODE10 = []
DI_AlarmCODE11 = []
DI_AlarmCODE12 = []
DI_AlarmCODE13 = []
DI_AlarmCODE14 = []
DI_AlarmCODE15 = []
DI_AlarmCODE16 = []
DI_AlarmCODE17 = []
DI_AlarmCODE18 = []
DI_AlarmCODE19 = []
DI_AlarmCODE20 = []
DI_AlarmCODE21 = []
DI_AlarmCODE22 = []
DI_AlarmCODE23 = []
DI_AlarmCODE24 = []
DI_AlarmCODE25 = []
DI_AlarmCODE26 = []
DI_AlarmCODE27 = []
DI_AlarmCODE28 = []
DI_AlarmCODE29 = []
DI_AlarmCODE30 = []
DI_AlarmCODE31 = []
DI_AlarmCODE32 = []
DI_AlarmCODE33 = []
DI_AlarmCODE34 = []
DI_AlarmCODE35 = []
DI_AlarmCODE36 = []
DI_AlarmCODE37 = []
DI_AlarmCODE38 = []
DI_AlarmCODE39 = []
DI_AlarmCODE40 = []
DI_AlarmCODE41 = []
DI_AlarmCODE42 = []
DI_AlarmCODE43 = []
DI_AlarmCODE44 = []
DI_AlarmCODE45 = []
DI_AlarmCODE46 = []
DI_AlarmCODE47 = []
DI_AlarmCODE48 = []
DI_AlarmCODE49 = []
DI_AlarmCODE50 = []
DI_AlarmCODE51 = []
DI_AlarmCODE52 = []
#
HR_VENTILATION_MODE = []
HR_MaxSPEED_MODE = []
HR_SPEED_MODE = []
#
real_time = time.strftime('%y-%m-%d %H:%M:%S')
host_client = "192.168.1.220"
c = ModbusClient()
if not c.host(host_client):
    print("host error")
if not c.port(502):
    print("port error")

# Автоматическое соединение TCP по запросу Modbus, закрытие после него\TCP auto connect on modbus request, close after it
c = ModbusClient(host=host_client, auto_open=True, auto_close=True)

while True:
    if c.is_open():
        #    считываем регистры установки\read setup registers
        in_regs_read = c.read_input_registers(0, 51)
        hl_regs_read = c.read_holding_registers(0, 3)
        coil_regs_read = c.read_coils(0, 25)
        dis_in_regs = c.read_discrete_inputs(0, 72)
#       присвоить переменным значение\assign variables a value
        CL_POWER, CL_TIMER, CL_WEEK, CL_Boost_MODE, CL_FPLC_MODE, CL_IntRH_CTRL, CL_ExtRH_CTRL, CL_IntCO2_CTRL, CL_ExtCO2_CTRL, CL_IntPM2_5_CTRL, CL_ExtPM2_5_CTRL, CL_IntVOC_CTRL, CL_ExtVOC_CTRL, CL_BoostSWITCH_CTRL, CL_FplcSWITCH_CTRL, CL_FireALARM_CTRL, CL_10V_SENSOR_CTRL, CL_RESET_FILTER_TIMER, CL_RESET_ALARM, CL_RESTORE_FACTORY, CL_CLOUD_CTRL, CL_MinSuAirOutTEMP_CTRL, CL_WaterPRESS_CTRL, CL_WaterFLOW_CTRL, CL_WaterHeaterAutoRestart = coil_regs_read
        IR_CurSelTEMP, IR_CurTEMP_SuAirIn, IR_CurTEMP_SuAirOut, IR_CurTEMP_ExAirIn, IR_CurTEMP_ExAirOut, unknown6in, unknown7in, IR_CurTEMP_Ext, IR_CurTEMP_Water, IR_CurVBAT, IR_CurRH_Int, IR_CurRH_Ext, IR_CurCO2_Int, IR_CurCO2_Ext, IR_CurPM2_5_Int, IR_CurPM2_5_Ext, IR_CurVOC_Int, IR_CurVOC_Ext, IR_Cur10V_SENSOR, IR_CurSuAirFLOW, IR_CurExAirFLOW, IR_CurSuPRESS, IR_CurExPRESS, IR_SuRPM, IR_ExRPM, unknown26in, IR_CurTIMER_TIME, unknown28in, IR_CurFILTER_TIMER, unknown30in, IR_TotalWorkingTime, IR_StateFILTER, IR_CurWeekSpeed, IR_CurWeekSetTemp, unknown35in, unknown36in, IR_VerMAIN_FMW, IR_DeviceTYPE, IR_ALARM, IR_RH_U, IR_CO2_U, IR_PM2_5_U, IR_VOC_U, IR_PreHeater_U, IR_MainHeater_U, IR_BPS_ROTOR_U, IR_KKB_U, IR_ReturnWater_U, IR_SuAirOutSetTemp, IR_WaterStandbySetTemp, IR_WaterStartSetTemp = in_regs_read
        DI_CurBoostSWITCH, DI_CurFplcSWITCH, DI_CurFireALARM, DI_StatusRH, DI_StatusCO2, DI_StatusPM2_5, DI_StatusVOC, DI_StatusHEATER, DI_StatusCOOLER, DI_StatusFanBLOWING, DI_CurPreHeaterThermostat, DI_CurMainHeaterThermostat, DI_CurSuFilterPRESS, DI_CurExFilterPRESS, DI_CurWaterPRESS, DI_CurWaterFLOW, DI_CurSuFanPRESS, DI_CurExFanPRESS, DI_WaterPreheatingStatus, DI_AlarmCODE0, DI_AlarmCODE1, DI_AlarmCODE2, DI_AlarmCODE3, DI_AlarmCODE4, DI_AlarmCODE5, DI_AlarmCODE6, DI_AlarmCODE7, DI_AlarmCODE8, DI_AlarmCODE9, DI_AlarmCODE10, DI_AlarmCODE11, DI_AlarmCODE12, DI_AlarmCODE13, DI_AlarmCODE14, DI_AlarmCODE15, DI_AlarmCODE16, DI_AlarmCODE17, DI_AlarmCODE18, DI_AlarmCODE19, DI_AlarmCODE20, DI_AlarmCODE21, DI_AlarmCODE22, DI_AlarmCODE23, DI_AlarmCODE24, DI_AlarmCODE25, DI_AlarmCODE26, DI_AlarmCODE27, DI_AlarmCODE28, DI_AlarmCODE29, DI_AlarmCODE30, DI_AlarmCODE31, DI_AlarmCODE32, DI_AlarmCODE33, DI_AlarmCODE34, DI_AlarmCODE35, DI_AlarmCODE36, DI_AlarmCODE37, DI_AlarmCODE38, DI_AlarmCODE39, DI_AlarmCODE40, DI_AlarmCODE41, DI_AlarmCODE42, DI_AlarmCODE43, DI_AlarmCODE44, DI_AlarmCODE45, DI_AlarmCODE46, DI_AlarmCODE47, DI_AlarmCODE48, DI_AlarmCODE49, DI_AlarmCODE50, DI_AlarmCODE51, DI_AlarmCODE52 = dis_in_regs
        HR_VENTILATION_MODE, HR_MaxSPEED_MODE, HR_SPEED_MODE = hl_regs_read
        print("Время", real_time)
        print("Время", type(real_time))
        #          тест списков :)
        #        print("количество значений списка переменних", len(other))
        print("количество значений списка регистров", type(hl_regs_read))
        print(CL_POWER)
        print(IR_CurSelTEMP)
        print(DI_StatusHEATER)
        print(HR_SPEED_MODE)
    else:
        c.open()
        time.sleep(2)
