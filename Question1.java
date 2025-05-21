package Trial;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Question1 {
    public static void main(String[] args) throws IOException {
        String[][] excelData = getData("C:\\Users\\mssrao\\Downloads\\EmpData.xlsx", "Sheet1");
        for (int i = 0; i < excelData.length; i++) {
            for (int j = 0; j < excelData[i].length; j++) {
                System.out.print(excelData[i][j] + "    ");
            }
            System.out.println();
        }
    }

    public static String[][] getData(String fileName, String sheetName) throws IOException, FileNotFoundException {
        File file = new File(fileName);
        FileInputStream ips = new FileInputStream(file);
        Workbook wb = new XSSFWorkbook(ips);
        Sheet sh = wb.getSheet(sheetName);
        int rowNumber = sh.getLastRowNum() + 1;
        int colNumber = sh.getRow(0).getLastCellNum();
        String[][] data = new String[rowNumber][colNumber];

        for (int i = 0; i < rowNumber; i++) {
            Row row = sh.getRow(i);
            for (int j = 0; j < colNumber; j++) {
                Cell cell = row.getCell(j);
                String value = new DataFormatter().formatCellValue(cell);
                data[i][j] = value;

            }
        }
        wb.close();
        return data;
    }
}
