document.addEventListener('DOMContentLoaded', function () {
    const sendButton = document.getElementById('send');
    sendButton.addEventListener('click', function () {
        // 获取用户输入的数据
        const news_id = document.getElementById('news_id').value;
        const context = document.getElementById('context').value;

        // 创建要发送到后端的数据对象
        const data = {
            "news_id": news_id,
            "context": context
        };

        console.log(data);

        // 发送数据到 Flask 服务器
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // 处理从后端返回的数据，例如将标题和短句显示在页面上
            const titlesAndContexts = data.datas;
            console.log(titlesAndContexts);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});