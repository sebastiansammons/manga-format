# template_css.py
stylesheet = """html{color:#000;background:#FFF;}body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,textarea,p,blockquote,th,td{margin:0;padding:0;}table{border-collapse:collapse;border-spacing:0;}fieldset,img{border:0;}address,caption,cite,code,dfn,em,strong,th,var{font-style:normal;font-weight:normal;}li{list-style:none;}caption,th{text-align:left;}h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:normal;}q:before,q:after{content:'';}abbr,acronym{border:0;font-variant:normal;}sup{vertical-align:text-top;}sub{vertical-align:text-bottom;}input,textarea,select{font-family:inherit;font-size:inherit;font-weight:inherit;}

div.fs {
        height: [HEIGHT]px;
        width: [WIDTH]px;
        position: relative;
}

div.fs a {
        display: block;
        width : 100%;
        height: 100%;
}

div.fs div {
        position: absolute;
}

img.singlePage {
        position: absolute;
        width: [WIDTH]px;
        height: auto;
}

"""
