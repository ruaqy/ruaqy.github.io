function PageHome () {
	var iframe = document.getElementById("subpage")
	iframe.src = "./post.html#pages/home.md";
}

function PageArtist(){
	var iframe = document.getElementById("subpage")
	iframe.src = "./post.html#pages/article.md";
}

function PageProject(){
	var iframe = document.getElementById("subpage")
	iframe.src = "./post.html#pages/project.md";
}

function PageAbout () {
	// 从markdown转化为html文件
	var iframe = document.getElementById("subpage")
	iframe.src = "./post.html#pages/about.md";
}