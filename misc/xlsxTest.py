import xlsxwriter
lumxLocation = 'C:\\Users\hariprasads\\Downloads\\Channel.lumx' #You lumx file location here
packageLocation = (lumxLocation.split(".")[0])
outputXLSX = packageLocation + "\\Detailed.xlsx"
# workbook = xlsxwriter.Workbook(outputXLSX)
# dataSourceWS = workbook.add_worksheet('Sheet1')
#
# workbook.close()


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook((outputXLSX))
worksheet = workbook.add_worksheet('sources')

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()