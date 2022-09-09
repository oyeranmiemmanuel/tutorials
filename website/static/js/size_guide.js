function downloadUsingAnchorElement(){
    const anchor= document.createElement("a");
    anchor.href= "Size Guides/men_shirt_measureguide.pdf";
    anchor.download= 'size_guide.pdf';

    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);

}