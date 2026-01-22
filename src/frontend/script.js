const imageInput = document.getElementById('imageInput');
const previewContainer = document.getElementById('previewContainer');
const imagePreview = document.getElementById('imagePreview');
const predictBtn = document.getElementById('predictBtn');
const resultContainer = document.getElementById('resultContainer');
const resultLabel = document.getElementById('resultLabel');
const confidenceBar = document.getElementById('confidenceBar');
const confidenceText = document.getElementById('confidenceText');
const loading = document.getElementById('loading');

// Khi chọn ảnh
imageInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        // Đọc và hiện ảnh preview
        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            previewContainer.classList.remove('d-none');
            predictBtn.classList.remove('d-none');
            // Ẩn kết quả cũ nếu có
            resultContainer.classList.add('d-none');
        }
        reader.readAsDataURL(file);
    }
});

// Khi bấm nút nhận diện
predictBtn.addEventListener('click', async function() {
    const file = imageInput.files[0];
    if (!file) return;

    // Hiển thị loading, ẩn nút
    loading.classList.remove('d-none');
    predictBtn.classList.add('d-none');
    resultContainer.classList.add('d-none');

    // Đóng gói ảnh để gửi
    const formData = new FormData();
    formData.append('file', file);

    try {
        // Gửi sang Backend
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        // Tắt loading
        loading.classList.add('d-none');
        predictBtn.classList.remove('d-none');

        if (response.ok) {
            // Hiện kết quả
            resultContainer.classList.remove('d-none');
            
            // Tên con vật
            const labelMap = {
                'cat': 'Con Mèo',
                'dog': 'Con Chó',
                'chicken': 'Con Gà',
                'cow': 'Con Bò',
                'horse': 'Con Ngựa'
            };
            resultLabel.textContent = labelMap[data.label] || data.label;

            // Độ chính xác
            const percent = Math.round(data.confidence * 100);
            confidenceBar.style.width = `${percent}%`;
            confidenceText.textContent = `${percent}%`;
            
            // Đổi màu thanh dựa trên độ tin cậy
            if(percent > 80) confidenceBar.className = "progress-bar bg-success";
            else if(percent > 50) confidenceBar.className = "progress-bar bg-warning";
            else confidenceBar.className = "progress-bar bg-danger";

        } else {
            alert('Lỗi: ' + (data.error || 'Không nhận diện được'));
        }

    } catch (error) {
        console.error(error);
        loading.classList.add('d-none');
        predictBtn.classList.remove('d-none');
        alert('Lỗi kết nối Server! Bạn đã bật Docker và Server chưa?');
    }
});