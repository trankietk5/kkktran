import kiet  
import quyet
import tri
import truong
import quyen
import Quan

def menu():
    while True:
        print("\n---------QUAN LY MON HOC---------")
        print("1. Môn học")
        print("2. Giảng viên")
        print("3. Sinh viên")
        print("4. Đăng ký học")
        print("5. Chuyên ngành")
        print("6. Kỳ học")
        print("0. Thoat")

        try:

            chon = float(input("Moi chon chuong trinh: "))
            if chon == 1:
                xac_nhan = input("Bạn có chắc chắn muốn chọn chương trình môn học? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã chọn chương trình: Môn học ")
                    kiet.menu()  
                else:
                    print("Đã hủy chương trình: Môn học")
                
            elif chon == 2:
                xac_nhan = input("Bạn có chắc chắn muốn chọn chương trình giảng viên? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã chọn chương trình: Giảng viên ")
                    quyet.show_menu()
                else:
                    print("Đã hủy chương trình: Giảng viên ")

            elif chon == 3:
                xac_nhan = input("Bạn có chắc chắn muốn chọn chương trình sinh viên ? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã chọn chương trình: Sinh viên")
                    truong.menu()
                else:
                    print("Đã hủy chương trình: Sinh viên ")
                    
               
                
            elif chon == 4:
                xac_nhan = input("Bạn có chắc chắn muốn chọn chương trình đăng ký học? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã chọn chương trình: Đăng ký học ")
                    Quan.display_menu()
                else:
                    print("Đã hủy chọn chương trình: Đăng ký học")
                
                
            elif chon == 5:
                xac_nhan = input("Bạn có chắc chắn muốn chọn chương trình chuyên ngành? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã chọn chương trình: Chuyên ngành")
                    quyen.display_menu()
                else:
                    print("Đã hủy chương trình: Chuyên ngành")
            
            elif chon == 6:
                xac_nhan = input("Bạn có chắc chắn muốn chọn chương trình kỳ học? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã chọn chương trình: Kỳ học")
                    tri.chon_chuc_nang()
                else:
                    print("Đã hủy chương trình: Kỳ học")  
                
            elif chon == 0:
                xac_nhan = input("Bạn có chắc chắn muốn chọn thoát? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã thoát chương trình")
                    break 
                else:
                    print("Đã hủy thoát")
                
            else: 
                print("Vui lòng nhập số từ (1-5), không nhập ký tự")
        
        except ValueError:
            print("Vui lòng nhập số từ (1-5), không nhập ký tự")

menu()
