function PageHome () {
	var iframe = document.getElementById("subpage")
	iframe.src = "./home.html";
}

function PageArtist(){
	var iframe = document.getElementById("subpage")
	iframe.src = "./artist.html";
}

function PageProject(){
	var iframe = document.getElementById("subpage")
	iframe.src = "./project.html";
}

function PageAbout () {
	// var iframe = document.getElementById("subpage")
	// iframe.src = "./about.html";
	
	// 从markdown转化为html文件
	var iframe = document.getElementById("subpage")
	iframe.src = "./post.html#pages/about.md";
}