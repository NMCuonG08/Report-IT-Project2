## :rocket:  qwen2
          
Use a `multi-page PDF` and a query related to multiple pages.

query = "`Quy chế đào tạo Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh`"

![image](https://github.com/user-attachments/assets/1ce980b6-8983-4c65-a8bc-182232c56ec6)

## :rocket:  mxbai-embed-large

![image](https://github.com/user-attachments/assets/a11c176e-8655-486b-b9c0-f6259ac01f64)


## :rocket:  Model: jina/jina-embeddings-v2-base-en

![image](https://github.com/user-attachments/assets/1f5b0423-a62e-4a7f-97f3-86fdb14d8a00)


## :rocket:  Model:  nomic-embed-text

![image](https://github.com/user-attachments/assets/f2bf1704-6526-4b61-94c2-8d1832d1dd91)

` Xếp hạng:`   jina/jina-embeddings-v2-base-en  >  nomic-embed-text  >  mxbai-embed-large  >  qwen2


`Đánh giá :` 
> jina/jina-embeddings-v2-base-en: Mô hình chủ yếu tập trung vào tạo embeddings cho văn bản nên có chất lượng rất cao  .
> 
> nomic-embed-text: Mô hình này có chất lượng khá cao. Chất lượng có thể phụ thuộc vào loại dữ liệu mà nó đã được huấn luyện.
> 
>  mxbai-embed-large: Mô hình này  được sử dụng cho các tác vụ cần độ chính xác cao. Chất lượng của nó có thể cao hơn nếu được huấn luyện trên tập dữ liệu phong phú.
> 
>  qwen2: Đây là mô hình mới nên chất lượng chưa được tốt lắm . 


# Kết quả lấy từ retriever.

## :rocket:  qwen2
          
Use a `multi-page PDF` and a query related to multiple pages.

query = "`Quy chế đào tạo Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh`"

![image](https://github.com/user-attachments/assets/44acfc6a-b9d4-4703-98f0-3c274510bd57)



## :rocket:  mxbai-embed-large

![image](https://github.com/user-attachments/assets/04004312-512e-4314-a473-4f23acba298e)




## :rocket:  Model: jina/jina-embeddings-v2-base-en

![image](https://github.com/user-attachments/assets/3ff96a0c-4bf9-43fb-8956-762dcdf51144)





## :rocket:  Model:  nomic-embed-text

![image](https://github.com/user-attachments/assets/58214151-0149-4ad3-9789-3f31f02b5638)


` Xếp hạng:`   jina/jina-embeddings-v2-base-en  >  nomic-embed-text  >  mxbai-embed-large  >  qwen2

` Đánh giá `: 

>  Sét về tổng quan thì khi thực hiện bằng code thông thường sẽ đưa ra các giá trị `Cosine Similarity` với trang có điểm cao nhất sẽ cao hơn một chút so với khi thực hiện lấy kết quả lấy từ retriever và sẽ là cùng trang. Nhưng từ các trang có số điểm từ thứ 2 trở đi sẽ có xu hướng khá là khác nhau khi nó chỉ chênh lệnh với nhau môt vài phần trăm điểm.

> Sự khác biệt nhỏ trong Cosine Similarity giữa các trang kế tiếp có thể tạo ra sự không đồng nhất trong thứ hạng. Điều này có nghĩa là retriever và code thông thường có thể nhạy cảm với những thay đổi nhỏ trong ngữ cảnh hoặc cấu trúc của các trang, dẫn đến kết quả không giống nhau ở các vị trí không phải là cao nhất.








