import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
public class File1{
  public static void main(String[] args){
	File file =new File("E:\\yuhengjob\\Newproject\\novel");
	if (!file.exists()){/*�ж��ļ����Ƿ����*/
		file.mkdir();/*�½��ļ���*/
	}
	for (int i=31;i<45;i++){
	try{
		BufferedWriter bw=new BufferedWriter(new FileWriter("E:\\yuhengjob\\Newproject\\novel\\"+i+"#new"+i+".txt"));
		bw.write("��"+i+"��"+"\r\n" +"������������ǰѼ��������������������������������������������������������");//���ļ���д������
		bw.close();//�ر��ļ�
	} catch (IOException e){
		e.printStackTrace();
	}
	}
}
}