function createLink(url, title) {
  const a = document.createElement("a");
  a.href = url;
  a.target = "_self";   // or remove the target line completely
  const favicon = document.createElement("img");
  favicon.src = "https://www.google.com/s2/favicons?sz=64&domain_url=" + url;
  a.appendChild(favicon);
  a.appendChild(document.createTextNode(title));
  return a;
}

function createFolder(name, children) {
  const div = document.createElement("div");
  div.classList.add("folder");
  const title = document.createElement("h2");
  title.textContent = name;
  div.appendChild(title);
  children.forEach(child => div.appendChild(child));
  return div;
}

function processBookmarks(nodes) {
  // Filter out unwanted folders
  const validNodes = nodes.filter(n => n.title !== "Other Bookmarks" && n.title !== "All Bookmarks");

  // Separate folders and links
  const folders = validNodes.filter(n => n.children && n.children.length);
  const links = validNodes.filter(n => n.url);

  // Sort alphabetically
  folders.sort((a, b) => a.title.localeCompare(b.title, undefined, { sensitivity: "base" }));
  links.sort((a, b) => (a.title || a.url).localeCompare(b.title || b.url, undefined, { sensitivity: "base" }));

  // Render
  const elements = [];

  // First folders
  for (const folder of folders) {
    const children = processBookmarks(folder.children);
    elements.push(createFolder(folder.title, children));
  }

  // Then links
  for (const link of links) {
    elements.push(createLink(link.url, link.title || link.url));
  }

  return elements;
}

chrome.bookmarks.getTree((tree) => {
  const bookmarksContainer = document.getElementById("bookmarks");
  const mainNodes = tree[0].children[0].children || [];
  const content = processBookmarks(mainNodes);
  content.forEach(el => bookmarksContainer.appendChild(el));
});
