import csv
import os

questions = [
    {
        "QuestionContent": "Giao kết hợp đồng điện tử là sự thỏa thuận về quyền và nghĩa vụ thông qua việc sử dụng gì?",
        "AAnsver": "Sự thỏa thuận bằng lời nói",
        "BAnswer": "Sự trao đổi văn bản trên giấy",
        "CAnswer": "Sự thỏa thuận bằng dữ liệu",
        "DAnswer": "Việc người mua thanh toán tiền trước",
        "Answer": "C"
    },
    {
        "QuestionContent": "Đặc điểm nổi bật nào của hợp đồng điện tử khác với hợp đồng truyền thống?",
        "AAnsver": "Phải có chữ tay trực tiếp để chứng thực",
        "BAnswer": "Bắt buộc thanh toán bằng tiền mặt khi nhận",
        "CAnswer": "Luôn phải gặp mặt trực tiếp để đàm phán giá",
        "DAnswer": "Khả năng tự động hóa không cần con người",
        "Answer": "D"
    },
    {
        "QuestionContent": "Đặc điểm ưu việt nhất của giao kết hợp đồng điện tử là gì?",
        "AAnsver": "Luôn phải dùng tiền mặt thanh toán",
        "BAnswer": "Không cần sự hiện diện vật lý",
        "CAnswer": "Phải có chữ ký tay các bên liên quan",
        "DAnswer": "Việc giải quyết tranh chấp dễ hơn",
        "Answer": "B"
    },
    {
        "QuestionContent": "Để một hợp đồng điện tử được xác lập, hai yếu tố cấu thành không thể tách rời là gì?",
        "AAnsver": "Người mua và người bán hàng",
        "BAnswer": "Chữ ký tay và con dấu tròn",
        "CAnswer": "Sự đề nghị và sự chấp nhận",
        "DAnswer": "Tiền mặt và chứng từ hóa đơn",
        "Answer": "C"
    },
    {
        "QuestionContent": "Một banner quảng cáo ghi 'Sale sập sàn, mại dô' trên website có được xem là lời đề nghị giao kết hợp lệ không?",
        "AAnsver": "Có hợp lệ vì nó hiển thị mức giá cực rẻ",
        "BAnswer": "Không vì nó chỉ là mời gọi",
        "CAnswer": "Có hợp lệ vì xuất hiện công khai trên mạng",
        "DAnswer": "Không vì nó chưa được chứng nhận bản quyền",
        "Answer": "B"
    },
    {
        "QuestionContent": "Một thông tin sản phẩm trên website với mức giá rõ ràng và nút 'Mua ngay' được pháp luật xem là gì?",
        "AAnsver": "Đề nghị giao kết hợp lệ",
        "BAnswer": "Một lời mời gọi đàm phán chung chung",
        "CAnswer": "Một hành vi mang tính quảng cáo thuần",
        "DAnswer": "Một thông báo hết hàng tạm thời của shop",
        "Answer": "A"
    },
    {
        "QuestionContent": "Trong nguyên tắc pháp lý về chấp nhận giao kết, sự im lặng của người mua được xem là gì?",
        "AAnsver": "Là sự đồng ý ngầm với điều kiện",
        "BAnswer": "Là sự từ chối mọi cuộc đàm phán",
        "CAnswer": "Không mặc nhiên coi là đồng ý",
        "DAnswer": "Là sự chờ đợi để giảm giá thêm",
        "Answer": "C"
    },
    {
        "QuestionContent": "Khi người mua gửi email: 'Giá máy 150 ngàn nhưng miễn phí ship nhé' đáp lại chào hàng, hành động này là gì?",
        "AAnsver": "Hành động này là sự chấp nhận giao kết",
        "BAnswer": "Đây là hành động vi phạm luật dân sự pháp",
        "CAnswer": "Đây là sự hủy bỏ hoàn toàn các thỏa thuận",
        "DAnswer": "Là một lời đề nghị giao kết mới",
        "Answer": "D"
    },
    {
        "QuestionContent": "Tọa độ pháp lý về địa điểm giao kết hợp đồng điện tử được xác định dựa trên yếu tố nào?",
        "AAnsver": "Nơi đặt máy chủ của hệ thống vận hành web",
        "BAnswer": "Nơi cư trú của người đề nghị",
        "CAnswer": "Nơi người mua bấm máy tính lúc chốt mua",
        "DAnswer": "Nơi kho hàng đang cất trữ món hàng thực",
        "Answer": "B"
    },
    {
        "QuestionContent": "Nếu doanh nghiệp VN thuê máy chủ tại Singapore để bán hàng, khi có tranh chấp, chọn địa điểm áp dụng luật ở đâu?",
        "AAnsver": "Tại nước Singapore do phải theo vị trí server",
        "BAnswer": "Tại Việt Nam nơi có trụ sở",
        "CAnswer": "Tại quốc gia cư trú của người mua sản phẩm",
        "DAnswer": "Tại tòa án thuộc quốc tế giải quyết chung",
        "Answer": "B"
    },
    {
        "QuestionContent": "Thời điểm giao kết hợp đồng điện tử được xác lập chính xác vào lúc nào?",
        "AAnsver": "Khi người dùng hoàn thiện ấn nút thanh toán",
        "BAnswer": "Khi thông điệp vào máy nhận",
        "CAnswer": "Khi người bán lên trang web đọc được tin",
        "DAnswer": "Khi shipper điện thoại hẹn giờ mang tới",
        "Answer": "B"
    },
    {
        "QuestionContent": "Trong 3 nguyên tắc 'vàng' của giao kết hợp đồng, nguyên tắc 'Tự do' có ý nghĩa gì?",
        "AAnsver": "Được quyền tự do trả giá món hàng thoải mái",
        "BAnswer": "Quyền dùng phương tiện số hay ko",
        "CAnswer": "Khách hàng có quyền hủy giao dịch vào mọi lúc",
        "DAnswer": "Cho phép tự do phát tán thông tin người dùng",
        "Answer": "B"
    },
    {
        "QuestionContent": "Việc hệ thống yêu cầu tích 'Tôi đồng ý với các điều khoản' trước khi thanh toán thể hiện nguyên tắc nào?",
        "AAnsver": "Thể hiện nguyên tắc Bảo mật an toàn",
        "BAnswer": "Thể hiện nguyên tắc Tự do lựa chọn",
        "CAnswer": "Thể hiện nguyên tắc Minh bạch",
        "DAnswer": "Thể hiện nguyên tắc Bảo vệ pháp lý",
        "Answer": "C"
    },
    {
        "QuestionContent": "Trong giao kết HĐĐT, nguyên tắc 'Bảo vệ' thường được hệ thống thực thi thông qua cơ chế nào?",
        "AAnsver": "Việc mã hóa thẻ tín dụng người dùng an toàn",
        "BAnswer": "Tính năng kiểm tra giỏ hàng",
        "CAnswer": "Yêu cầu đền bù tiền mặt gấp đôi cho bên mua",
        "DAnswer": "Chức năng chặn tin nhắn quảng cáo tự động",
        "Answer": "B"
    },
    {
        "QuestionContent": "Một hợp đồng B2C hoàn chỉnh thông thường bao gồm chu trình khép kín mấy bước?",
        "AAnsver": "Khép kín qua đúng 3 bước",
        "BAnswer": "Khép kín qua đúng 4 bước",
        "CAnswer": "Có 5 bước khép kín",
        "DAnswer": "Khép kín qua đúng 6 bước",
        "Answer": "C"
    },
    {
        "QuestionContent": "Một hợp đồng B2C chỉnh chu thực sự kết thúc vào thời điểm nào?",
        "AAnsver": "Khi người mua thao tác hoàn tất ấn đặt hàng",
        "BAnswer": "Khi khâu thanh toán tiền được thực hiện xong",
        "CAnswer": "Khi shipper giao ngay hàng tới tay người mua",
        "DAnswer": "Khi hết thời hạn bảo hành của nó",
        "Answer": "D"
    },
    {
        "QuestionContent": "Khi khách hàng click 'Place Order' trên web, dưới góc độ pháp lý, khách hàng đang thực hiện hành vi gì?",
        "AAnsver": "Đây là sự chấp nhận mã hóa gửi đi",
        "BAnswer": "Hành vi đưa ra Đề nghị",
        "CAnswer": "Khởi đầu hành động hủy bỏ giao dịch",
        "DAnswer": "Lời từ chối nhận món hàng đó",
        "Answer": "B"
    },
    {
        "QuestionContent": "Khi hệ thống tự động gửi email 'Order Confirmed', lúc này hợp đồng điện tử có trạng thái gì?",
        "AAnsver": "Nó hoàn toàn chưa có hiệu lực mặt pháp lý",
        "BAnswer": "Hợp đồng chỉ mới dừng ở lời mời đàm phán",
        "CAnswer": "Hợp đồng có hiệu lực pháp lý",
        "DAnswer": "Mới chỉ là lời tự động thông báo của server",
        "Answer": "C"
    },
    {
        "QuestionContent": "Hình thức thanh toán COD (Nhận hàng trả tiền) mang lại điều gì cho doanh nghiệp bán hàng?",
        "AAnsver": "Đem lại quy trình nhận chuyển tiền nhanh nhất",
        "BAnswer": "Giúp cho chủ shop cắt giảm chi phí nhiều nhất",
        "CAnswer": "Mang lại sự an toàn bảo mật tuyệt đối trăm phần",
        "DAnswer": "Tiềm ẩn rủi ro bom hàng cao",
        "Answer": "D"
    },
    {
        "QuestionContent": "Thuật ngữ 3PL trong khâu thực thi giao hàng điện tử là gì?",
        "AAnsver": "Vận chuyển trung gian",
        "BAnswer": "Mã số định danh mã hóa của người tiêu dùng",
        "CAnswer": "Hình thức để thanh toán ngân hàng trực tuyến",
        "DAnswer": "Chính sách cấp chứng nhận bảo hành sản phẩm",
        "Answer": "A"
    },
    {
        "QuestionContent": "Yếu tố nào kết nối thế giới thực của shipper với thế giới ảo của hệ thống TMĐT?",
        "AAnsver": "Ký nhận bằng hình thức tờ phiếu trên giấy tờ",
        "BAnswer": "Mã Tracking Number",
        "CAnswer": "Thông điệp email thông báo khuyến mãi giảm giá",
        "DAnswer": "Chức năng ứng dụng quét mã QR để trả tiền nhanh",
        "Answer": "B"
    },
    {
        "QuestionContent": "Đặc điểm giao nhận của 'Hàng số' (như gói phim Netflix) khác với hàng vật lý là gì?",
        "AAnsver": "Yêu cầu bắt rành rẽ bưu điện gửi đi xác nhận",
        "BAnswer": "Thường sẽ mất vài ngày để vận chuyển đường xa",
        "CAnswer": "Phải chờ khi có người gọi điện thoại xác nhận",
        "DAnswer": "Giao tức thời ngay sau khi mua",
        "Answer": "D"
    },
    {
        "QuestionContent": "Quyền lợi của khách hàng khi shop giao sai màu áo đã đặt trên hệ thống TMĐT là gì?",
        "AAnsver": "Phải âm thầm cam chịu trận mà không được trả",
        "BAnswer": "Chỉ việc im lặng vào web và đánh giá sao thấp",
        "CAnswer": "Quyền yêu cầu đổi trả hoàn toàn",
        "DAnswer": "Khách mua món mới để bù trừ lỗi của người bán",
        "Answer": "C"
    },
    {
        "QuestionContent": "Trong HĐĐT, quyền lợi bảo hành sản phẩm thường được chứng minh bằng gì thay thế phiểu giấy?",
        "AAnsver": "Hóa đơn trên máy và lịch sử",
        "BAnswer": "Dùng chính ảnh chụp lại màn hình lúc đặt đơn",
        "CAnswer": "Tin nhắn trao đổi qua lại với người giao hàng",
        "DAnswer": "Giấy in bản sao kê đối soát tài khoản ngân hàng",
        "Answer": "A"
    },
    {
        "QuestionContent": "Việc hệ thống tự gửi mã giảm giá email sau vài ngày mua hàng nằm trong khâu nào?",
        "AAnsver": "Nó nằm trong bước khởi đầu Đặt hàng",
        "BAnswer": "Nằm trong khâu Xác nhận hệ thống",
        "CAnswer": "Nó thuộc về khâu Giao nhận vận tải",
        "DAnswer": "Thuộc khâu Hậu mãi cuối",
        "Answer": "D"
    },
    {
        "QuestionContent": "Đâu là điểm khác biệt lớn nhất về khâu 'Ký kết' trong hợp đồng B2B so với B2C?",
        "AAnsver": "Ở điểm chỉ cần tự nhấn tick nút ô Đồng ý là xong",
        "BAnswer": "Bắt buộc để lại chữ ký văn bản tay của hai bên",
        "CAnswer": "Phải dùng chữ ký số USB Token",
        "DAnswer": "Hai bên gặp mặt không cần chữ ký nào để hợp lệ",
        "Answer": "C"
    },
    {
        "QuestionContent": "Hoạt động 'Thương lượng về giá sỉ, mức chiết khấu từng nấc' thuộc khâu nào trong hợp đồng B2B?",
        "AAnsver": "Thuộc khâu Đàm phán",
        "BAnswer": "Thuộc nội dung khâu Ký kết",
        "CAnswer": "Nó nằm trong khâu Thực thi",
        "DAnswer": "Được tính vào khâu Hậu mãi",
        "Answer": "A"
    },
    {
        "QuestionContent": "Trình tự đúng của chuỗi sự kiện khi mua hàng thanh toán online bằng quét QR là gì?",
        "AAnsver": "Khởi đầu là Đề nghị, Giao nhận, Thanh toán...",
        "BAnswer": "Đề nghị, Thanh toán, Xác nhận, Giao nhận",
        "CAnswer": "Phải qua Xác nhận, Thanh toán, Giao nhận...",
        "DAnswer": "Bắt đầu Thanh toán, Xác nhận, Giao nhận...",
        "Answer": "B"
    },
    {
        "QuestionContent": "Trong ví dụ mua sắm, việc xuất 'Hóa đơn điện tử' cuối cùng đóng vai trò gì?",
        "AAnsver": "Nó dùng đánh dấu là hành vi đang chốt mua đơn",
        "BAnswer": "Là thủ tục chứng từ hoàn tất",
        "CAnswer": "Nhằm mục đích là để người tiêu dùng kiểm tra kĩ",
        "DAnswer": "Dùng làm bước việc tự động cấp quyền để truy cập",
        "Answer": "B"
    },
    {
        "QuestionContent": "Theo phân tích, hợp đồng điện tử có giá trị pháp lý ra sao so với hợp đồng chữ ký tay?",
        "AAnsver": "Giá trị của nó yếu hơn rất nhiều so với văn bản",
        "BAnswer": "Trong thực tế nó hoàn toàn không có hiệu lực gì",
        "CAnswer": "Có hiệu lực tương đương",
        "DAnswer": "Chỉ thực sự có tác dụng ràng buộc mua hàng nhỏ",
        "Answer": "C"
    }
]

headers = ["ID", "CourseContentId", "IdContent", "QuestionType", "QuestionContent", "AAnsver", "BAnswer", "CAnswer", "DAnswer", "Answer", "ResultAnswer", "Explanation"]

output_file = r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Chuong_2_Tiet_2_30_cau.csv'

with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for idx, q in enumerate(questions):
        ans_key = q["Answer"]
        if ans_key == "A":
            ans_val = q["AAnsver"]
        elif ans_key == "B":
            ans_val = q["BAnswer"]
        elif ans_key == "C":
            ans_val = q["CAnswer"]
        else:
            ans_val = q["DAnswer"]
            
        writer.writerow({
            "ID": idx + 1,
            "CourseContentId": "Chương 2. Giao kết hợp đồng điện tử",
            "IdContent": "2",
            "QuestionType": "1",
            "QuestionContent": q["QuestionContent"],
            "AAnsver": q["AAnsver"],
            "BAnswer": q["BAnswer"],
            "CAnswer": q["CAnswer"],
            "DAnswer": q["DAnswer"],
            "Answer": q["Answer"],
            "ResultAnswer": ans_val,
            "Explanation": f"Đáp án chính xác là: {ans_val}. Vui lòng ôn tập lại nội dung Tiết học này để nắm vững kiến thức."
        })
print(f"Successfully generated 30 questions at {output_file}")
