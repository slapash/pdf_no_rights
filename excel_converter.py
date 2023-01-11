from win32com import client
import os
path = os.getcwd()
def convert_to_pdf(file):
    global path
    global wb
    app = client.DispatchEx("Excel.Application")
    app.Visible = False
    app.Interactive = False
    wb = app.Workbooks.Open(file)
    try:
        count = wb.Sheets.Count
        for i in range(count + 1):
            ws=wb.Worksheets(i + 1)
            ws.ExportAsFixedFormat(0, path + "\\" + f'fichier{i}' )
        
        wb.Close()
    except:
        print( "code failed")
        wb.Close()

'''
Worksheets("Sheet1").Activate 
ActiveSheet.PageSetup.Orientation = xlLandscape
count = wb.Sheets.Count
'''