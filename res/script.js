

function uploadContent() {

    // If textarea value changes.
    if (content !== textarea.value) {
        var temp = textarea.value;
        var request = new XMLHttpRequest();
        if(temp=="")setTimeout(uploadContent, 1000);
        else{
            request.open('POST', window.location.href, true);
            request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
            request.onload = function() {
                if (request.readyState === 4) {

                    // Request has ended, check again after 1 second.
                    content = temp;
                    setTimeout(uploadContent, 1000);
                }
            }
            request.onerror = function() {

                // Try again after 1 second.
                setTimeout(uploadContent, 1000);
            }
            request.send('text=' + encodeURIComponent(temp));
            {//更新预览
                var splitDiv = document.getElementById("split-div");
                if (splitDiv != null&&splitDiv.style.display === "block") {
                    var contentText = document.getElementById("text-box").value;
                    var converter = new showdown.Converter();
                    //设置markdown转换器的选项
                    converter.setOption('tables', true);
                    converter.setOption('tasklists', true);
                    converter.setOption('footnotes', true);
                    converter.setOption('simplifiedAutoLink', true);
                    converter.setOption('strikethrough', true);
                    //进行转换
                    var htmlContent = converter.makeHtml(contentText);
                    splitDiv.innerHTML = htmlContent;
                }
            }
            // Make the content available to print.
            printable.removeChild(printable.firstChild);
            printable.appendChild(document.createTextNode(temp));
        }
    }
    else {

        // Content has not changed, check again after 1 second.
        setTimeout(uploadContent, 1000);
    }
}

var textarea = document.getElementById("text-box");
var printable = document.getElementById('printable');

// Make the content available to print.
printable.appendChild(document.createTextNode(content));
textarea.focus();
uploadContent();

