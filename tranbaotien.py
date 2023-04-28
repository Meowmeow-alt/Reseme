import streamlit as st
from PIL import Image

st.set_page_config(page_title = "Trần Bảo Tiên CV",
                   page_icon = ":smiling_face_with_3_hearts:",
                   layout = "wide")

def css(file):
     with open(file) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css("style/style.css")

# ___________ MỞ ĐẦU _____________

with st.container():
     st.write("---")
     leftcol, gap, mid, rightcol = st.columns((1,0.2,2,1))
     with mid:
          st.title("Trần Bảo Tiên")
          st.subheader("Học sinh THPT Chuyên Lê Hồng Phong 	:point_right:	:point_left: :heart_on_fire:")
          st.write(" 12CV1 (Chuyên Văn 1)")
          st.write("- Bảo Tiên cực kì thích học code và tạo ra nhiều thứ thú vị.")
          st.write("- Bảo Tiên vô cùng thiếu nghị lực và không thể giận ai được quá lâu.")
          st.write("- Bảo Tiên thích uống rau má sữa, ăn bánh ngọt và hay tò mò~ :cake: :sparkles:")
          st.write("[Tìm hiểu thêm qua link facebook >](https://www.facebook.com/baotiendancer/)")
     with leftcol:
          img2 = Image.open("Images/122407738_2286976264780882_1017126760838664431_n.jpeg")
          st.image(img2)
     with rightcol:
          img1 = Image.open("Images/118766465_2222042181274291_3183358602759430686_n.jpeg")
          st.image(img1)
     with gap:
          gap.empty()

#_____________PHẦN 1_______________

with st.container():
     st.write("---")
     gap1, leftcol, gap2, rightcol = st.columns((0.2,0.7,0.2,2))
     with rightcol:
          st.header("Những hoạt động em từng tham gia")
          st.write("##")
          st.write("""
          Từ nhỏ em đã là một học sinh rất chăm và năng động trong việc tham gia các hoạt động chung :woman-bowing:
          - Thứ nhất: Liên Đội Phó Tiểu học Bàu Sen, chỉ huy Đội giỏi cấp Quận. :star:
          - Thứ hai: Cháu ngoan Bác Hồ cấp Thành Phố 3 năm liền. :star:
          - Thứ ba: Cựu thành viên Hội đồng trẻ em Thành Phố Hồ Chí Minh. :star:
          - Thứ tư: Giải Khiêu vũ thể thao giải mở rộng Toàn Quốc 2015 - 2 huy chương vàng, 1 huy chương bạc. :star:
          - Thứ năm: Giải Wushu mở rộng Toàn Thành 2015 (Võ Thuật) - Huy chương bạc. :star:
          - Thứ sáu: Câu lạc bộ khiêu vũ Thể Thao 116 Nguyễn Du - Trợ Giảng. :star:
          - Thứ bảy: Chương trình Mầm Chồi Lá (POPS KID) - Diễn viên nhí. :star:
          - Thứ tám: Báo Khăn Quàng Đỏ - Cộng tác viên viết báo, phóng viên nhí. :star:
          - Thứ chín: Thành viên Đội Văn Nghệ THPT Chuyên Lê Hồng Phong. :star:
          - Thứ mười: Đậu 3 bảng tuyển sinh: Lê Hồng Phong, Nguyễn Thị Minh Khai, THTH Đại học Sư Phạm. :star:
          """
               )
     with gap2:
          st.write(":heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n:heart:\n\n")
     with leftcol:
          img7 = Image.open("Images//z4302489122192_179145a8528f5f66964e369f78b6f23e.jpg")
          st.image(img7)
     with gap1:
          gap1.empty()

st.write("###")
st.write("---")

#_____________PHẦN 2____________

with st.container():
     leftcol, midcol, rightcol = st.columns((2,0.7,1.04))
     with midcol:
          img_b = Image.open("Images/z4302410330167_291e5a958594b941ba84b4e5c1b28669.jpg")
          st.image(img_b)
     with leftcol:
          st.header("Vì sao nên chọn Bảo Tiên?")
          st.write("##")
          st.write("""
          Trường sẽ không bao giờ tìm thấy ai đáng yêu hơn Bảo Tiên trên hành tinh xanh này! :earth_africa:
          - Thứ nhất: Em hứa sẽ học thật giỏi và đem nhiều thành tích về! :star:
          - Thứ hai: Em ngoan và chịu tiếp thu. :star:
          - Thứ ba: Em luôn cố gắng trong mọi việc em làm và vô cùng có trách nhiệm. :star:
          - Thứ tư: Em mong được trường chấp nhận và trở thành học sinh của trường. 	:star:
          Đây là trang web em tự mình viết ra bằng code, thông qua thư viện streamlit.\n
          Vì em mong có thể gây ấn tượng với Ban tuyển sinh của trường. :rainbow:
          """
               )
     with rightcol:
          img_a = Image.open("Images/z4302409456331_5cc53c89635c9ca5d02d9706b50d463b.jpg")
          st.image(img_a)

st.write("###")
st.write("---")

#_____________PHẦN 3______________

st.header(" >> Kênh Youtube của Bảo Tiên :heart:")
st.write("###")
with st.container():
     leftcol, mid, rightcol = st.columns((1,0.2,2))
     with leftcol:
          img3 = Image.open("Images/A.png")
          st.image(img3)
     with mid:
          mid.empty()
     with rightcol:
          st.subheader("[Màu nắng >](https://youtu.be/KM1yRCvGtXI)")
          st.write("###")
          st.write("Video về một lần đến vườn hoa hướng dương của Bảo Tiên.")

st.write("###")
with st.container():
     leftcol, mid, rightcol = st.columns((1,0.2,2))
     with leftcol:
          img3 = Image.open("Images/B.png")
          st.image(img3)
     with mid:
          mid.empty()
     with rightcol:
          st.subheader("[Bảo tàng Thành Phố Hồ Chí Minh >](https://youtu.be/HwifyPzl1TE)")
          st.write("###")
          st.write("Video về một lần đến Bảo tàng Thành Phố của Bảo Tiên.")

#____________LỜI NHẮN____________

with st.container():
     st.write("###")
     st.write("---")
     st.header("Điều mà trường muốn nhắn gửi tới em?")
     st.write("###")
     contact = """
     <form action="https://formsubmit.co/chenchen31105@gmail.com" method="POST">
     <input type="hidden" name = "_captcha" value="false">
     <input type="text" name="name" placeholder="Tên ban đại diện" required>
     <input type="email" name="email" placeholder="Email ban đại diện" required>
     <textarea name="message" placeholder="Nội dung thư gửi đến email của Bảo Tiên" required></textarea>
     <button type="submit">Send</button>
     </form>
     """
     leftcol, rightcol = st.columns((0.8,2))
     with leftcol:
          st.markdown(contact, unsafe_allow_html=True)
     with rightcol:
          st.empty()