# Animeverse Chronicles - Multiverse War

Animeverse Chronicles là game chiến thuật thủ thành. Mỗi người chơi cần triệu hồi những nhân vật mạnh mẽ của mình ra để chiến đấu với đối thủ. Mục đích tối thượng là tiêu diệt nhà chính đối thủ để dành chiến thắng.

Game có hai chế độ chơi là chế độ PvC(Người với Máy) và PvP(Người với Người).
Chế độ chơi PvP, người chơi bên trái sẽ sử dụng chuột, bên phải sử dụng bàn phím.

Cách chơi:
+   Đối với dùng chuột: 
    Ấn chuột vào nhân vật để triệu hồi khi đủ tiền, ấn vào nút nâng cấp hình mũi tên lên để lên level cho nhà chính, và ấn vào nhân vật để chọn nhân vật bạn muốn nâng cấp.
+   Đối với dùng bàn phím: 
    Ấn các phím từ 1 đến 6 để triệu hồi các nhân vật tương ứng. Ấn P để lên level cho nhà chính, sau đó ấn các phím từ 1 đến 6 để nâng cấp cho nhân vật bạn muốn tương ứng.

Di chuột vào nhân vật để hiện ra bảng thông số chi tiết của nhân vật. Ấn chuột trái vào nhân 
vật để bật bảng thông số, ấn chuột phải ra ngoài để tắt.

Tiền vàng trong game sẽ được dùng để triệu hồi nhân vật, lên cấp.
Người chơi sẽ được 5 vàng mỗi giây.

Có 6 nhân vật bao gồm: Swordman, Archer, Tanker, Wizard, Goku, Naruto.

Giá tiền mỗi cấp:

	tanker:20/30/45/70/100
	swordman:30/50/70/90/120
	archer:40/65/90/110/150
	wizard:50/70/100/135/170
	Goku: 350/400/500
	Naruto: 350/550

Có 20 cấp tất cả, có thể dùng tiền để lên cấp. Mỗi khi lên 1 cấp sẽ được tăng máu cho nhà chính và có thể chọn tăng cấp cho 1 nhân vật bất kỳ nếu nhân vật đó chưa max cấp.

Giá tiền để lên cấp lần lượt là:

    200, 250, 280, 300, 320, 350, 380, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1150, 1250, 1350, 1500


Cấp độ tối đa: 

    swordman:5
	archer:5
	tanker:5
	wizard:5
	Goku: 3
	Naruto: 2

Mỗi nhân vật khi lên cấp sẽ được tăng sức mạnh(máu/dame/tốc đánh/…)
Chỉ số các nhân vật từng cấp:

	Swordman: 
		Máu: 200.0/ 250.0/ 500.0/ 600.0/ 1000.0
		Sát thương đánh thường: 50.0/55.0/100.0/110.0/200.0
		Tốc độ đánh: 2.5s / 1 đòn
		Kỹ năng đặc biệt: chém 2 đòn liên tiếp mỗi đòn hồi cho bản thân 20% máu tối đa .
	

	Archer: 
		Máu: 100.0/ 120.0/ 150.0/ 170.0/ 200.0
		Sát thương đánh thường :20.0/ 30.0 / 50.0/ 50.0 / 50.0
		Tốc độ đánh: 2/ 1.75/ 1 / 1/  1  (giây / 1 đòn)
			+level 3 và 4 bắn ra 2 tên 1 lần
			+level 5  bắn ra 3 tên 1 lần
		Kỹ năng đặc biệt: bắn ra mũi tên đặc biệt có hiệu ứng xuyên thấu (mũi tên tăng 100% dame nếu level <= 2 và xuyên tối đa 3 mục tiêu) sau đó tăng 100% tốc bắn trong vòng 4s tiếp
	

	Tanker :
		Máu: 500.0/ 600.0/ 1200.0/ 1500.0/ 3000.0
		Sát thương đánh thường :10.0 / 20.0/ 45.0 / 50.0/  70.0
		Tốc độ đánh: 6s / 1 đòn
		Kỹ năng đặc biệt: miễn thương 40.0/ 45.0/ 70.0/ 65.0/ 90.0 % trong vòng 6s , nếu level >= 3 sẽ có thêm miễn khống trong 3s
	

	Wizard:
		Máu: 100.0/ 120.0/ 160.0/ 180.0/ 250.0
		Sát thương đánh thường :10.0/ 10.0 / 20.0/ 25.0 / 40.0
		Tốc độ đánh: 2s / 1 đòn
		Mana mỗi đòn đánh trúng: 25/ 30/ 50/ 50/ 50
		Kỹ năng đặc biệt: rút hồn kẻ địch gần nhất gây 20% máu tối đa của 1 mục tiêu (số lượng tăng theo cấp) thành sát thương sau đó gây choáng 1s và đẩy lùi mục tiêu. Số mục tiêu bị dính hiệu ứng tăng theo cấp: 1/ 1/ 1/ 2/ 5 (mục tiêu). Sau đẩy lùi lập tức vung chổi và hồi máu cho đồng minh trước mặt lượng máu tăng theo cấp :40/ 50/ 80/ 100/ 200
	

	Naruto:
		Máu: 300.0/ 600.0
		Sát thương đánh thường :50.0/ 100.0
		Tốc độ đánh: 1s / 1 đòn
			+ở dạng đánh gần :đánh 3 đòn liên tiếp,đòn đánh thường thứ 3 hất tung nhẹ
			+ở dạng đánh xa: phi phi tiêu gây sát thương
		Kỹ năng đặc biệt:
			+Level 1: miễn khống trong 5s đồng thời triệu hồi 5 phân thân (chỉ số tương đương bản thân nhưng những đòn đánh thường không hất tung) sau 5s phân thân nếu không chết sẽ tự biến mất
			+Level 2;miễn khống trong thời gian tung chiêu, triệu hồi 5 phân thân tương tự level 1 sau đó kết ấn tạo rasenshuriken phóng ra đẩy lùi kẻ địch và ở cuối cùng phát nổ .Suốt quá trình này gây 5.0 sát thương mỗi 0.1 giây
	

	Goku:
		Máu: 1000.0/ 1500.0/ 3000.0
		Sát thương đánh thường :100.0/ 200.0 / 300.0
		Tốc độ đánh: 2s / 1 đòn
		Sát thương kame :15.0/20.0/30.0
		Kỹ năng đặc biệt:
			+Level 1: miễn khống trong thời gian tung chiêu, đá đẩy lùi mục tiêu trước mặt sau đó bắn kame theo chiều ngang gây sát thương mỗi 0.1 giây
			+Level 2: miễn khống trong thời gian tung chiêu, đá đẩy lùi mục tiêu trước mặt và đánh dấu mục tiêu đó sau đó nhảy đến trước mặt mục tiêu đá hất tung lên khỏi mặt đất rồi tung chưởng kame chéo gây sát thương mỗi 0.1 giây
			+Level 3: miễn khống trong thời gian tung chiêu, đá đẩy lùi mục tiêu trước mặt và đánh dấu mục tiêu đó sau đó bắn kame theo chiều ngang gây sát thương mỗi 0.1 giây và tiếp tục nhảy đến trước mặt mục tiêu bị đánh dấu đá hất tung lên khỏi mặt đất rồi tung chưởng kame chéo  gây sát thương mỗi  0.1 giây, sau đó dịch chuyển về vị trí đầu hàng.
