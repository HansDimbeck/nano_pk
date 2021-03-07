# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:22:58 2021

@author: Tobias
"""


from apscheduler.schedulers.background import BackgroundScheduler
from telnetlib import Telnet
from datetime import datetime
import xml.etree.ElementTree as xml




class HargassnerMessageTemplates:

    NANO_V14K = "NANO_V14K"
    NANO_V14L = "NANO_V14L"

    DICT = {
        NANO_V14K : "<DAQPRJ><ANALOG><CHANNEL id='0' name='ZK' unit=''/><CHANNEL id='1' name='O2' unit='%'/><CHANNEL id='2' name='O2soll' unit='%'/><CHANNEL id='3' name='TK' unit='°C'/><CHANNEL id='4' name='TKsoll' unit='°C'/><CHANNEL id='5' name='TRG' unit='°C'/><CHANNEL id='6' name='SZist' unit='%'/><CHANNEL id='7' name='SZsoll' unit='%'/><CHANNEL id='8' name='Leistung' unit='%'/><CHANNEL id='9' name='ESsoll' unit='%'/><CHANNEL id='10' name='I Es' unit='mA'/><CHANNEL id='11' name='I Ra' unit='mA'/><CHANNEL id='12' name='I Aa' unit='mA'/><CHANNEL id='13' name='I Sr' unit='mA'/><CHANNEL id='14' name='I Rein' unit='mA'/><CHANNEL id='15' name='Taus' unit='°C'/><CHANNEL id='16' name='TA Gem.' unit='°C'/><CHANNEL id='17' name='TPo' unit='°C'/><CHANNEL id='18' name='TPmo' unit='°C'/><CHANNEL id='19' name='TPm' unit='°C'/><CHANNEL id='20' name='TPmu' unit='°C'/><CHANNEL id='21' name='TPu' unit='°C'/><CHANNEL id='22' name='TFW' unit='°C'/><CHANNEL id='23' name='TRL' unit='°C'/><CHANNEL id='24' name='TRLsoll' unit='°C'/><CHANNEL id='25' name='Tplat' unit='°C'/><CHANNEL id='26' name='BRT' unit='°C'/><CHANNEL id='27' name='Regler K' unit=''/><CHANNEL id='28' name='KeBrstScale' unit='%'/><CHANNEL id='29' name='ESRegler' unit='%'/><CHANNEL id='30' name='BLDC_ES ist' unit='rpm'/><CHANNEL id='31' name='BLDC_ES soll' unit='rpm'/><CHANNEL id='32' name='LZ ES seit Füll.' unit='Min'/><CHANNEL id='33' name='LZ ES seit Ent.' unit='Min'/><CHANNEL id='34' name='Anzahl Entasch.' unit=''/><CHANNEL id='35' name='Anzahl SR Beweg.' unit=''/><CHANNEL id='36' name='Heiz P Lambda' unit='W'/><CHANNEL id='37' name='Heiz U Lambda' unit='V'/><CHANNEL id='38' name='Heiz I Lambda' unit='mA'/><CHANNEL id='39' name='Sens U Lambda' unit='mV'/><CHANNEL id='40' name='PuffZustand' unit=''/><CHANNEL id='41' name='Puffer_soll' unit='°C'/><CHANNEL id='42' name='Puff Füllgrad' unit='%'/><CHANNEL id='43' name='max.Leist.P3F.HT' unit='%'/><CHANNEL id='44' name='Spreizung' unit='°C'/><CHANNEL id='45' name='AIN17' unit='V'/><CHANNEL id='46' name='Lagerstand' unit='kg'/><CHANNEL id='47' name='Verbrauchszähler' unit='kg'/><CHANNEL id='48' name='UsePos' unit=''/><CHANNEL id='49' name='Störungs Nr' unit=''/><CHANNEL id='50' name='TVL_A' unit='°C'/><CHANNEL id='51' name='TVLs_A' unit='°C'/><CHANNEL id='52' name='TRA_A' unit='°C'/><CHANNEL id='53' name='TRs_A' unit='°C'/><CHANNEL id='54' name='HKZustand_A' unit=''/><CHANNEL id='55' name='FRA Zustand' unit=''/><CHANNEL id='56' name='TVL_1' unit='°C'/><CHANNEL id='57' name='TVLs_1' unit='°C'/><CHANNEL id='58' name='TRA_1' unit='°C'/><CHANNEL id='59' name='TRs_1' unit='°C'/><CHANNEL id='60' name='HKZustand_1' unit=''/><CHANNEL id='61' name='FR1 Zustand' unit=''/><CHANNEL id='62' name='TVL_2' unit='°C'/><CHANNEL id='63' name='TVLs_2' unit='°C'/><CHANNEL id='64' name='TRA_2' unit='°C'/><CHANNEL id='65' name='TRs_2' unit='°C'/><CHANNEL id='66' name='HKZustand_2' unit=''/><CHANNEL id='67' name='FR2 Zustand' unit=''/><CHANNEL id='68' name='TVL_3' unit='°C'/><CHANNEL id='69' name='TVLs_3' unit='°C'/><CHANNEL id='70' name='TRA_3' unit='°C'/><CHANNEL id='71' name='TRs_3' unit='°C'/><CHANNEL id='72' name='HKZustand_3' unit=''/><CHANNEL id='73' name='FR3 Zustand' unit=''/><CHANNEL id='74' name='TVL_4' unit='°C'/><CHANNEL id='75' name='TVLs_4' unit='°C'/><CHANNEL id='76' name='TRA_4' unit='°C'/><CHANNEL id='77' name='TRs_4' unit='°C'/><CHANNEL id='78' name='HKZustand_4' unit=''/><CHANNEL id='79' name='FR4 Zustand' unit=''/><CHANNEL id='80' name='TVL_5' unit='°C'/><CHANNEL id='81' name='TVLs_5' unit='°C'/><CHANNEL id='82' name='TRA_5' unit='°C'/><CHANNEL id='83' name='TRs_5' unit='°C'/><CHANNEL id='84' name='HKZustand_5' unit=''/><CHANNEL id='85' name='FR5 Zustand' unit=''/><CHANNEL id='86' name='TVL_6' unit='°C'/><CHANNEL id='87' name='TVLs_6' unit='°C'/><CHANNEL id='88' name='TRA_6' unit='°C'/><CHANNEL id='89' name='TRs_6' unit='°C'/><CHANNEL id='90' name='HKZustand_6' unit=''/><CHANNEL id='91' name='FR6 Zustand' unit=''/><CHANNEL id='92' name='TBA' unit='°C'/><CHANNEL id='93' name='TBs_A' unit='°C'/><CHANNEL id='94' name='BoiZustand_A' unit=''/><CHANNEL id='95' name='TB1' unit='°C'/><CHANNEL id='96' name='TBs_1' unit='°C'/><CHANNEL id='97' name='BoiZustand_1' unit=''/><CHANNEL id='98' name='TB2' unit='°C'/><CHANNEL id='99' name='TBs_2' unit='°C'/><CHANNEL id='100' name='BoiZustand_2' unit=''/><CHANNEL id='101' name='TB3' unit='°C'/><CHANNEL id='102' name='TBs_3' unit='°C'/><CHANNEL id='103' name='BoiZustand_3' unit=''/><CHANNEL id='104' name='Ext.HK Soll' unit=''/><CHANNEL id='105' name='Ext.HK Soll_2' unit=''/><CHANNEL id='106' name='Ext.HK Soll_3' unit=''/><CHANNEL id='107' name='Höchste Anf' unit=''/><CHANNEL id='108' name='Anf. HKR0' unit='°C'/><CHANNEL id='109' name='Anf. HKR1' unit='°C'/><CHANNEL id='110' name='Anf. HKR2' unit='°C'/><CHANNEL id='111' name='Anf. HKR3' unit='°C'/><CHANNEL id='112' name='Anf. HKR4' unit='°C'/><CHANNEL id='113' name='Anf. HKR5' unit='°C'/><CHANNEL id='114' name='Anf. HKR6' unit='°C'/><CHANNEL id='115' name='Anf. HKR7' unit='°C'/><CHANNEL id='116' name='Anf. HKR8' unit='°C'/><CHANNEL id='117' name='Anf. HKR9' unit='°C'/><CHANNEL id='118' name='Anf. HKR10' unit='°C'/><CHANNEL id='119' name='Anf. HKR11' unit='°C'/><CHANNEL id='120' name='Anf. HKR12' unit='°C'/><CHANNEL id='121' name='Anf. HKR13' unit='°C'/><CHANNEL id='122' name='Anf. HKR14' unit='°C'/><CHANNEL id='123' name='Anf. HKR15' unit='°C'/><CHANNEL id='124' name='KaskSollTmp_1' unit='°C'/><CHANNEL id='125' name='KaskSollTmp_2' unit='°C'/><CHANNEL id='126' name='KaskSollTmp_3' unit='°C'/><CHANNEL id='127' name='KaskSollTmp_4' unit='°C'/><CHANNEL id='128' name='KaskIstTmp_1' unit='°C'/><CHANNEL id='129' name='KaskIstTmp_2' unit='°C'/><CHANNEL id='130' name='KaskIstTmp_3' unit='°C'/><CHANNEL id='131' name='KaskIstTmp_4' unit='°C'/><CHANNEL id='132' name='T Spülung' unit='°C'/><CHANNEL id='133' name='DiffReg S1' unit='°C'/><CHANNEL id='134' name='DiffReg S2' unit='°C'/><CHANNEL id='135' name='TVG' unit='°C'/><CHANNEL id='136' name='WMZ_1_TVL' unit='°C'/><CHANNEL id='137' name='WMZ_1_TRL' unit='°C'/><CHANNEL id='138' name='WMZ_1_PWR' unit='kW'/><CHANNEL id='139' name='WMZ_1_FLOW' unit='l/h'/><CHANNEL id='140' name='WMZ_2_TVL' unit='°C'/><CHANNEL id='141' name='WMZ_2_TRL' unit='°C'/><CHANNEL id='142' name='WMZ_2_PWR' unit='kW'/><CHANNEL id='143' name='WMZ_2_FLOW' unit='l/h'/><CHANNEL id='144' name='WMZ_3_TVL' unit='°C'/><CHANNEL id='145' name='WMZ_3_TRL' unit='°C'/><CHANNEL id='146' name='WMZ_3_PWR' unit='kW'/><CHANNEL id='147' name='WMZ_3_FLOW' unit='l/h'/><CHANNEL id='148' name='WMZ_4_TVL' unit='°C'/><CHANNEL id='149' name='WMZ_4_TRL' unit='°C'/><CHANNEL id='150' name='WMZ_4_PWR' unit='kW'/><CHANNEL id='151' name='WMZ_4_FLOW' unit='l/h'/><CHANNEL id='152' name='WMZ_5_TVL' unit='°C'/><CHANNEL id='153' name='WMZ_5_TRL' unit='°C'/><CHANNEL id='154' name='WMZ_5_PWR' unit='kW'/><CHANNEL id='155' name='WMZ_5_FLOW' unit='l/h'/><CHANNEL id='156' name='WMZ_6_TVL' unit='°C'/><CHANNEL id='157' name='WMZ_6_TRL' unit='°C'/><CHANNEL id='158' name='WMZ_6_PWR' unit='kW'/><CHANNEL id='159' name='WMZ_6_FLOW' unit='l/h'/><CHANNEL id='160' name='FWS1 Anf.' unit='°C'/><CHANNEL id='161' name='FWS1 Pumpe' unit='%'/><CHANNEL id='162' name='FWS1 Leist' unit='kW'/><CHANNEL id='163' name='FWS1 T' unit='°C'/><CHANNEL id='164' name='FWS1 D' unit='l/min'/><CHANNEL id='165' name='FWS2 Anf.' unit='°C'/><CHANNEL id='166' name='FWS2 Pumpe' unit='%'/><CHANNEL id='167' name='FWS2 Leist' unit='kW'/><CHANNEL id='168' name='FWS2 T' unit='°C'/><CHANNEL id='169' name='FWS2 D' unit='l/min'/><CHANNEL id='170' name='FWS3 Anf.' unit='°C'/><CHANNEL id='171' name='FWS3 Pumpe' unit='%'/><CHANNEL id='172' name='FWS3 Leist' unit='kW'/><CHANNEL id='173' name='FWS3 T' unit='°C'/><CHANNEL id='174' name='FWS3 D' unit='l/min'/><CHANNEL id='175' name='FWS4 Anf.' unit='°C'/><CHANNEL id='176' name='FWS4 Pumpe' unit='%'/><CHANNEL id='177' name='FWS4 Leist' unit='kW'/><CHANNEL id='178' name='FWS4 T' unit='°C'/><CHANNEL id='179' name='FWS4 D' unit='l/min'/><CHANNEL id='180' name='DiffReg2 S3' unit='°C'/><CHANNEL id='181' name='DiffReg2 S4' unit='°C'/></ANALOG><DIGITAL><CHANNEL id='0' bit='0' name='Stb'/><CHANNEL id='0' bit='1' name='Fuellstand'/><CHANNEL id='0' bit='3' name='Es Rein Endl'/><CHANNEL id='0' bit='4' name='HKPA'/><CHANNEL id='0' bit='5' name='MAA'/><CHANNEL id='0' bit='6' name='MAZ'/><CHANNEL id='0' bit='7' name='HKP1'/><CHANNEL id='0' bit='8' name='M1A'/><CHANNEL id='0' bit='9' name='M1Z'/><CHANNEL id='0' bit='10' name='HKP2'/><CHANNEL id='0' bit='11' name='M2A'/><CHANNEL id='0' bit='12' name='M2Z'/><CHANNEL id='0' bit='13' name='Störung'/><CHANNEL id='1' bit='0' name='L Heiz.'/><CHANNEL id='1' bit='1' name='Z Heiz.'/><CHANNEL id='1' bit='2' name='Z Geb.'/><CHANNEL id='1' bit='3' name='AA Run'/><CHANNEL id='1' bit='4' name='AA Dir'/><CHANNEL id='1' bit='5' name='ES Run'/><CHANNEL id='1' bit='6' name='ES Dir'/><CHANNEL id='1' bit='7' name='AS Saug'/><CHANNEL id='1' bit='8' name='AS RA Run'/><CHANNEL id='1' bit='9' name='AS RA Dir'/><CHANNEL id='1' bit='10' name='Rein En'/><CHANNEL id='1' bit='11' name='Rein Run'/><CHANNEL id='1' bit='12' name='RLm_auf'/><CHANNEL id='1' bit='13' name='RLm_zu'/><CHANNEL id='1' bit='14' name='RL Pumpe'/><CHANNEL id='2' bit='0' name='BPA'/><CHANNEL id='2' bit='1' name='BP1'/><CHANNEL id='2' bit='2' name='BP2'/><CHANNEL id='2' bit='3' name='BP3'/><CHANNEL id='2' bit='4' name='BZPA'/><CHANNEL id='2' bit='5' name='BZP1'/><CHANNEL id='2' bit='6' name='BZP2'/><CHANNEL id='2' bit='7' name='BZP3'/><CHANNEL id='2' bit='8' name='EHKP'/><CHANNEL id='2' bit='9' name='EHKP2'/><CHANNEL id='2' bit='10' name='EHKP3'/><CHANNEL id='2' bit='11' name='EHK Anf'/><CHANNEL id='2' bit='12' name='EHK Anf2'/><CHANNEL id='2' bit='13' name='EHK Anf3'/><CHANNEL id='3' bit='0' name='HKP3'/><CHANNEL id='3' bit='1' name='M3A'/><CHANNEL id='3' bit='2' name='M3Z'/><CHANNEL id='3' bit='3' name='HKP4'/><CHANNEL id='3' bit='4' name='M4A'/><CHANNEL id='3' bit='5' name='M4Z'/><CHANNEL id='3' bit='6' name='HKP5'/><CHANNEL id='3' bit='7' name='M5A'/><CHANNEL id='3' bit='8' name='M5Z'/><CHANNEL id='3' bit='9' name='HKP6'/><CHANNEL id='3' bit='10' name='M6A'/><CHANNEL id='3' bit='11' name='M6Z'/><CHANNEL id='3' bit='13' name='PuffP'/><CHANNEL id='3' bit='14' name='Entasch gesp.'/><CHANNEL id='3' bit='15' name='ATW'/><CHANNEL id='4' bit='8' name='KASK1 Run'/><CHANNEL id='4' bit='9' name='KASK2 Run'/><CHANNEL id='4' bit='10' name='KASK3 Run'/><CHANNEL id='4' bit='11' name='KASK4 Run'/><CHANNEL id='4' bit='12' name='FW Freig.'/><CHANNEL id='4' bit='13' name='sAS Anf Füll'/><CHANNEL id='4' bit='14' name='HKV'/><CHANNEL id='4' bit='15' name='FLP'/><CHANNEL id='5' bit='5' name='Netztrafo'/><CHANNEL id='5' bit='6' name='Netzrelais'/><CHANNEL id='5' bit='7' name='Lagerraum'/><CHANNEL id='5' bit='8' name='Aschebox'/><CHANNEL id='6' bit='0' name='gFlP'/><CHANNEL id='6' bit='1' name='gFlM auf'/><CHANNEL id='6' bit='2' name='gFlM zu'/><CHANNEL id='6' bit='4' name='Spülung Aktiv'/><CHANNEL id='7' bit='0' name='DReg P1'/><CHANNEL id='7' bit='1' name='DReg P2'/><CHANNEL id='7' bit='2' name='DReg Mi auf'/><CHANNEL id='7' bit='3' name='DReg Mi zu'/><CHANNEL id='7' bit='4' name='Oel Out'/><CHANNEL id='7' bit='5' name='DReg2 P1'/><CHANNEL id='7' bit='6' name='DReg2 P2'/><CHANNEL id='7' bit='7' name='DReg2 Mi auf'/><CHANNEL id='7' bit='8' name='DReg2 Mi zu'/></DIGITAL></DAQPRJ>",
        NANO_V14L : "<DAQPRJ><ANALOG><CHANNEL id='0' name='ZK' unit=''/><CHANNEL id='1' name='O2' unit='%'/><CHANNEL id='2' name='O2soll' unit='%'/><CHANNEL id='3' name='TK' unit='°C'/><CHANNEL id='4' name='TKsoll' unit='°C'/><CHANNEL id='5' name='TRG' unit='°C'/><CHANNEL id='6' name='SZist' unit='%'/><CHANNEL id='7' name='SZsoll' unit='%'/><CHANNEL id='8' name='Leistung' unit='%'/><CHANNEL id='9' name='ESsoll' unit='%'/><CHANNEL id='10' name='I Es' unit='mA'/><CHANNEL id='11' name='I Ra' unit='mA'/><CHANNEL id='12' name='I Aa' unit='mA'/><CHANNEL id='13' name='I Sr' unit='mA'/><CHANNEL id='14' name='I Rein' unit='mA'/><CHANNEL id='15' name='Taus' unit='°C'/><CHANNEL id='16' name='TA Gem.' unit='°C'/><CHANNEL id='17' name='TPo' unit='°C'/><CHANNEL id='18' name='TPmo' unit='°C'/><CHANNEL id='19' name='TPm' unit='°C'/><CHANNEL id='20' name='TPmu' unit='°C'/><CHANNEL id='21' name='TPu' unit='°C'/><CHANNEL id='22' name='TFW' unit='°C'/><CHANNEL id='23' name='TRL' unit='°C'/><CHANNEL id='24' name='TRLsoll' unit='°C'/><CHANNEL id='25' name='Tplat' unit='°C'/><CHANNEL id='26' name='BRT' unit='°C'/><CHANNEL id='27' name='Regler K' unit=''/><CHANNEL id='28' name='KeBrstScale' unit='%'/><CHANNEL id='29' name='ESRegler' unit='%'/><CHANNEL id='30' name='BLDC_ES ist' unit='rpm'/><CHANNEL id='31' name='BLDC_ES soll' unit='rpm'/><CHANNEL id='32' name='LZ ES seit Füll.' unit='Min'/><CHANNEL id='33' name='LZ ES seit Ent.' unit='Min'/><CHANNEL id='34' name='Anzahl Entasch.' unit=''/><CHANNEL id='35' name='Anzahl SR Beweg.' unit=''/><CHANNEL id='36' name='Heiz P Lambda' unit='W'/><CHANNEL id='37' name='Heiz U Lambda' unit='V'/><CHANNEL id='38' name='Heiz I Lambda' unit='mA'/><CHANNEL id='39' name='Sens U Lambda' unit='mV'/><CHANNEL id='40' name='PuffZustand' unit=''/><CHANNEL id='41' name='Puffer_soll' unit='°C'/><CHANNEL id='42' name='Puff Füllgrad' unit='%'/><CHANNEL id='43' name='max.Leist.P3F.HT' unit='%'/><CHANNEL id='44' name='Spreizung' unit='°C'/><CHANNEL id='45' name='AIN17' unit='V'/><CHANNEL id='46' name='Lagerstand' unit='kg'/><CHANNEL id='47' name='Verbrauchszähler' unit='kg'/><CHANNEL id='48' name='UsePos' unit=''/><CHANNEL id='49' name='Störungs Nr' unit=''/><CHANNEL id='50' name='TVL_A' unit='°C'/><CHANNEL id='51' name='TVLs_A' unit='°C'/><CHANNEL id='52' name='TRA_A' unit='°C'/><CHANNEL id='53' name='TRs_A' unit='°C'/><CHANNEL id='54' name='HKZustand_A' unit=''/><CHANNEL id='55' name='FRA Zustand' unit=''/><CHANNEL id='56' name='TVL_1' unit='°C'/><CHANNEL id='57' name='TVLs_1' unit='°C'/><CHANNEL id='58' name='TRA_1' unit='°C'/><CHANNEL id='59' name='TRs_1' unit='°C'/><CHANNEL id='60' name='HKZustand_1' unit=''/><CHANNEL id='61' name='FR1 Zustand' unit=''/><CHANNEL id='62' name='TVL_2' unit='°C'/><CHANNEL id='63' name='TVLs_2' unit='°C'/><CHANNEL id='64' name='TRA_2' unit='°C'/><CHANNEL id='65' name='TRs_2' unit='°C'/><CHANNEL id='66' name='HKZustand_2' unit=''/><CHANNEL id='67' name='FR2 Zustand' unit=''/><CHANNEL id='68' name='TVL_3' unit='°C'/><CHANNEL id='69' name='TVLs_3' unit='°C'/><CHANNEL id='70' name='TRA_3' unit='°C'/><CHANNEL id='71' name='TRs_3' unit='°C'/><CHANNEL id='72' name='HKZustand_3' unit=''/><CHANNEL id='73' name='FR3 Zustand' unit=''/><CHANNEL id='74' name='TVL_4' unit='°C'/><CHANNEL id='75' name='TVLs_4' unit='°C'/><CHANNEL id='76' name='TRA_4' unit='°C'/><CHANNEL id='77' name='TRs_4' unit='°C'/><CHANNEL id='78' name='HKZustand_4' unit=''/><CHANNEL id='79' name='FR4 Zustand' unit=''/><CHANNEL id='80' name='TVL_5' unit='°C'/><CHANNEL id='81' name='TVLs_5' unit='°C'/><CHANNEL id='82' name='TRA_5' unit='°C'/><CHANNEL id='83' name='TRs_5' unit='°C'/><CHANNEL id='84' name='HKZustand_5' unit=''/><CHANNEL id='85' name='FR5 Zustand' unit=''/><CHANNEL id='86' name='TVL_6' unit='°C'/><CHANNEL id='87' name='TVLs_6' unit='°C'/><CHANNEL id='88' name='TRA_6' unit='°C'/><CHANNEL id='89' name='TRs_6' unit='°C'/><CHANNEL id='90' name='HKZustand_6' unit=''/><CHANNEL id='91' name='FR6 Zustand' unit=''/><CHANNEL id='92' name='TBA' unit='°C'/><CHANNEL id='93' name='TBs_A' unit='°C'/><CHANNEL id='94' name='BoiZustand_A' unit=''/><CHANNEL id='95' name='TB1' unit='°C'/><CHANNEL id='96' name='TBs_1' unit='°C'/><CHANNEL id='97' name='BoiZustand_1' unit=''/><CHANNEL id='98' name='TB2' unit='°C'/><CHANNEL id='99' name='TBs_2' unit='°C'/><CHANNEL id='100' name='BoiZustand_2' unit=''/><CHANNEL id='101' name='TB3' unit='°C'/><CHANNEL id='102' name='TBs_3' unit='°C'/><CHANNEL id='103' name='BoiZustand_3' unit=''/><CHANNEL id='104' name='Ext.HK Soll' unit=''/><CHANNEL id='105' name='Ext.HK Soll_2' unit=''/><CHANNEL id='106' name='Ext.HK Soll_3' unit=''/><CHANNEL id='107' name='Höchste Anf' unit=''/><CHANNEL id='108' name='Anf. HKR0' unit='°C'/><CHANNEL id='109' name='Anf. HKR1' unit='°C'/><CHANNEL id='110' name='Anf. HKR2' unit='°C'/><CHANNEL id='111' name='Anf. HKR3' unit='°C'/><CHANNEL id='112' name='Anf. HKR4' unit='°C'/><CHANNEL id='113' name='Anf. HKR5' unit='°C'/><CHANNEL id='114' name='Anf. HKR6' unit='°C'/><CHANNEL id='115' name='Anf. HKR7' unit='°C'/><CHANNEL id='116' name='Anf. HKR8' unit='°C'/><CHANNEL id='117' name='Anf. HKR9' unit='°C'/><CHANNEL id='118' name='Anf. HKR10' unit='°C'/><CHANNEL id='119' name='Anf. HKR11' unit='°C'/><CHANNEL id='120' name='Anf. HKR12' unit='°C'/><CHANNEL id='121' name='Anf. HKR13' unit='°C'/><CHANNEL id='122' name='Anf. HKR14' unit='°C'/><CHANNEL id='123' name='Anf. HKR15' unit='°C'/><CHANNEL id='124' name='T Spülung' unit='°C'/><CHANNEL id='125' name='DiffReg S1' unit='°C'/><CHANNEL id='126' name='DiffReg S2' unit='°C'/><CHANNEL id='127' name='TVG' unit='°C'/><CHANNEL id='128' name='DiffReg2 S3' unit='°C'/><CHANNEL id='129' name='DiffReg2 S4' unit='°C'/><CHANNEL id='130' name='U Netzteil' unit='mV'/><CHANNEL id='131' name='TBB' unit='°C'/><CHANNEL id='132' name='TBs_B' unit='°C'/><CHANNEL id='133' name='BoiZustand_B' unit=''/><CHANNEL id='134' name='TVL_B' unit='°C'/><CHANNEL id='135' name='TVLs_B' unit='°C'/><CHANNEL id='136' name='TRB' unit='°C'/><CHANNEL id='137' name='TRs_B' unit='°C'/><CHANNEL id='138' name='HKZustand_B' unit=''/><CHANNEL id='139' name='TRA_B' unit='°C'/><CHANNEL id='140' name='FRB Zustand' unit=''/></ANALOG><DIGITAL><CHANNEL id='0' bit='0' name='Stb'/><CHANNEL id='0' bit='1' name='Fuellstand'/><CHANNEL id='0' bit='3' name='Es Rein Endl'/><CHANNEL id='0' bit='4' name='HKPA'/><CHANNEL id='0' bit='5' name='MAA'/><CHANNEL id='0' bit='6' name='MAZ'/><CHANNEL id='0' bit='7' name='HKP1'/><CHANNEL id='0' bit='8' name='M1A'/><CHANNEL id='0' bit='9' name='M1Z'/><CHANNEL id='0' bit='10' name='HKP2'/><CHANNEL id='0' bit='11' name='M2A'/><CHANNEL id='0' bit='12' name='M2Z'/><CHANNEL id='0' bit='13' name='Störung'/><CHANNEL id='1' bit='0' name='L Heiz.'/><CHANNEL id='1' bit='1' name='Z Heiz.'/><CHANNEL id='1' bit='2' name='Z Geb.'/><CHANNEL id='1' bit='3' name='AA Run'/><CHANNEL id='1' bit='4' name='AA Dir'/><CHANNEL id='1' bit='5' name='ES Run'/><CHANNEL id='1' bit='6' name='ES Dir'/><CHANNEL id='1' bit='7' name='AS Saug'/><CHANNEL id='1' bit='8' name='AS RA Run'/><CHANNEL id='1' bit='9' name='AS RA Dir'/><CHANNEL id='1' bit='10' name='Rein En'/><CHANNEL id='1' bit='11' name='Rein Run'/><CHANNEL id='1' bit='12' name='RLm_auf'/><CHANNEL id='1' bit='13' name='RLm_zu'/><CHANNEL id='1' bit='14' name='RL Pumpe'/><CHANNEL id='2' bit='0' name='BPA'/><CHANNEL id='2' bit='1' name='BP1'/><CHANNEL id='2' bit='2' name='BP2'/><CHANNEL id='2' bit='3' name='BP3'/><CHANNEL id='2' bit='4' name='BZPA'/><CHANNEL id='2' bit='5' name='BZP1'/><CHANNEL id='2' bit='6' name='BZP2'/><CHANNEL id='2' bit='7' name='BZP3'/><CHANNEL id='2' bit='8' name='EHKP'/><CHANNEL id='2' bit='9' name='EHKP2'/><CHANNEL id='2' bit='10' name='EHKP3'/><CHANNEL id='2' bit='11' name='EHK Anf'/><CHANNEL id='2' bit='12' name='EHK Anf2'/><CHANNEL id='2' bit='13' name='EHK Anf3'/><CHANNEL id='3' bit='0' name='HKP3'/><CHANNEL id='3' bit='1' name='M3A'/><CHANNEL id='3' bit='2' name='M3Z'/><CHANNEL id='3' bit='3' name='HKP4'/><CHANNEL id='3' bit='4' name='M4A'/><CHANNEL id='3' bit='5' name='M4Z'/><CHANNEL id='3' bit='6' name='HKP5'/><CHANNEL id='3' bit='7' name='M5A'/><CHANNEL id='3' bit='8' name='M5Z'/><CHANNEL id='3' bit='9' name='HKP6'/><CHANNEL id='3' bit='10' name='M6A'/><CHANNEL id='3' bit='11' name='M6Z'/><CHANNEL id='3' bit='13' name='PuffP'/><CHANNEL id='3' bit='14' name='Entasch gesp.'/><CHANNEL id='3' bit='15' name='ATW'/><CHANNEL id='4' bit='0' name='HKPB'/><CHANNEL id='4' bit='1' name='MBA'/><CHANNEL id='4' bit='2' name='MBZ'/><CHANNEL id='4' bit='3' name='BPB'/><CHANNEL id='4' bit='4' name='BZPB'/><CHANNEL id='4' bit='8' name='KASK1 Run'/><CHANNEL id='4' bit='9' name='KASK2 Run'/><CHANNEL id='4' bit='10' name='KASK3 Run'/><CHANNEL id='4' bit='11' name='KASK4 Run'/><CHANNEL id='4' bit='12' name='FW Freig.'/><CHANNEL id='4' bit='13' name='sAS Anf Füll'/><CHANNEL id='4' bit='14' name='HKV'/><CHANNEL id='4' bit='15' name='FLP'/><CHANNEL id='5' bit='5' name='Netztrafo'/><CHANNEL id='5' bit='6' name='Netzrelais'/><CHANNEL id='5' bit='7' name='Lagerraum'/><CHANNEL id='5' bit='8' name='Aschebox'/><CHANNEL id='6' bit='0' name='gFlP'/><CHANNEL id='6' bit='1' name='gFlM auf'/><CHANNEL id='6' bit='2' name='gFlM zu'/><CHANNEL id='6' bit='4' name='Spülung Aktiv'/><CHANNEL id='7' bit='0' name='DReg P1'/><CHANNEL id='7' bit='1' name='DReg P2'/><CHANNEL id='7' bit='2' name='DReg Mi auf'/><CHANNEL id='7' bit='3' name='DReg Mi zu'/><CHANNEL id='7' bit='4' name='Oel Out'/><CHANNEL id='7' bit='5' name='DReg2 P1'/><CHANNEL id='7' bit='6' name='DReg2 P2'/><CHANNEL id='7' bit='7' name='DReg2 Mi auf'/><CHANNEL id='7' bit='8' name='DReg2 Mi zu'/></DIGITAL></DAQPRJ>"
    }




class HargassnerParameter:
    
    _DESCRIPTIONS = { "ZK":"state", "O2":"o2", "O2soll":"o2 target", "TK":"boiler temperature", "TKsoll":"boiler temperature target", "TRG":"smoke gas temperature", 
                      "SZist":"draft", "SZsoll":"draft target", "Leistung":"output", "ESsoll":"delivery rate", "I Es":"drawer current", "I Sr":"grate current", "I Rein":"cleaning current",
                      "Taus":"outside temperature", "TA Gem.":"mean outside temperature", "TPo":"buffer temperature top", "TPm":"buffer temperature center", "TPu":"buffer temperature bottom",
                      "TRL":"return temperature", "TRLsoll":"return temperature target"}
    
    def __init__(self, key, index, unit):
        self._key = key
        self._index = index
        self._value = None
        self._unit = unit
        
    def __str__(self):
        if self.value(): return self.description() + " : " + self.value() + " " + self.unit()
        else: return self.description() + " : unknown"
    
    def key(self):
        return self._key
    
    def index(self):
        return self._index
            
    def value(self):
        return self._value
    
    def unit(self):
        return self._unit
    
    def description(self):
        return HargassnerParameter._DESCRIPTIONS.get(self.key(), self.key())


class HargassnerAnalogueParameter(HargassnerParameter):
    
    def __init__(self, key, index, unit):
        super().__init__(key, index, unit)
        
    def initializeFromMessage(self, msg):
        self._value = msg[self._index]


class HargassnerDigitalParameter(HargassnerParameter):
    
    def __init__(self, key, index, bitmask):
        super().__init__(key, index, "")
        self._bitmask = bitmask
    
    def initializeFromMessage(self, msg):
        self._value = (str)(((int)(msg[self._index], 16) & self._bitmask) > 0)




class HargassnerBridge:
       
    def __init__(self, hostIP, updateInterval=1.0, msgFormat=HargassnerMessageTemplates.NANO_V14L):
        self._hostIP = hostIP
        self._telnet = Telnet(hostIP)
        self._connectionOK = False
        self._latestUpdate = None
        self._paramData = {}
        self._expectedMsgLength = 0
        self._errorLog = ""
        self._infoLog = ""
        self.setMessageFormat(msgFormat)
        self._scheduler = BackgroundScheduler()
        if updateInterval<0.5: updateInterval=0.5 # Hargassner sends 2 messages per second, no need to poll more frequent than that
        self._scheduler.add_job(lambda:self._update(),'interval',seconds=updateInterval)
        self._scheduler.start()
        
    def setMessageFormat(self, msgFormat):
        if msgFormat in HargassnerMessageTemplates.DICT:
            msgFormat = HargassnerMessageTemplates.DICT[msgFormat] # if one of the constants has been passed, expand to full format string
        if not msgFormat.startswith("<DAQPRJ>"):
            self._errorLog += "HargassnerBridge.setMessageFormat(): Message template does not start with '<DAQPRJ>'.\n"
            return False
        self._paramData = {}
        root = xml.fromstring(msgFormat)
        analog = root.find("ANALOG")
        for channel in analog.findall("CHANNEL"):
            self._paramData[(str)(channel.get("name"))] = HargassnerAnalogueParameter( (str)(channel.get("name")), (int)(channel.get("id")), (str)(channel.get("unit")))
        ofsDigital = len(self._paramData) # assuming that channel ids/indices are listed consecutively without any misses!
        lenDigital = 0
        digital = root.find("DIGITAL")
        for channel in digital.findall("CHANNEL"):
            self._paramData[(str)(channel.get("name"))] = HargassnerDigitalParameter( (str)(channel.get("name")), ofsDigital + (int)(channel.get("id")),  1 << (int)(channel.get("bit")))
            lenDigital = (int)(channel.get("id")) + 1 # assuming that channel ids are increasing
        self._expectedMsgLength = ofsDigital + lenDigital
        self._infoLog += "HargassnerBridge.setMessageFormat(): successfully parsed " + (str)(self._expectedMsgLength) + " elements.\n"
        return True
        
    def close(self):
        self._infoLog += "HargassnerBridge.close(): Closing connection...\n"
        self._scheduler.shutdown()
        self._telnet.close()
        
    def _update(self):
        if self._connectionOK:
            try:
                data = self._telnet.read_very_eager()
            except EOFError as error:
                self._errorLog += "HargassnerBridge._update(): Telnet connection error (" + (str)(error) + ")\n"
                self._connectionOK = False
                return    
            msg = data.decode("ascii")
            lastMsgStart = msg.rfind("pm ")
            if lastMsgStart < 0: 
                self._infoLog += "HargassnerBridge._update(): Received message contains no data.\n"
                return
            msg = msg[lastMsgStart+3:-3].split(' ')
            if  len(msg) != self._expectedMsgLength:
                self._errorLog += "HargassnerBridge._update(): Received message has unexpected length.\n"
                return
            for param in self._paramData.values():
                param.initializeFromMessage(msg)
            self._latestUpdate = datetime.now()
        else:
            self._infoLog += "HargassnerBridge._update(): Opening connection...\n"
            self._telnet.open(self._hostIP)
            self._connectionOK = True
    
    def getValue(self, paramName):
        param = self._paramData.get(paramName)
        if param==None: 
            self._errorLog += "HargassnerBridge.getValue(): Parameter key " + paramName + " not known.\n"
            return None 
        return param.value()
    
    def getUnit(self, paramName):
        param = self._paramData.get(paramName)
        if param==None: 
            self._errorLog += "HargassnerBridge.getUnit(): Parameter key " + paramName + " not known.\n"
            return None 
        return param.unit()
    
    def data(self):
        return self._paramData
    
    def latestUpdateTime(self):
        return self._latestUpdate
    
    def getErrorLog(self):
        log = self._errorLog
        self._errorLog = ""
        return log
    
    def getInfoLog(self):
        log = self._infoLog
        self._infoLog = ""
        return log
