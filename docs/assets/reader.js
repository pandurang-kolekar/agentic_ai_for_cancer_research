async function loadCatalog() {
  const response = await fetch('catalog.json');
  if (!response.ok) {
    throw new Error('Unable to load catalog.json');
  }
  return response.json();
}

function queryId() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id');
}

function detectRepoBase() {
  if (window.BOOK_CONFIG && window.BOOK_CONFIG.repoUrl) {
    return window.BOOK_CONFIG.repoUrl.replace(/\/$/, '');
  }
  const host = window.location.hostname;
  const pathParts = window.location.pathname.split('/').filter(Boolean);
  if (!host.endsWith('.github.io')) {
    return null;
  }
  const owner = host.replace('.github.io', '');
  const repo = pathParts[0] || '';
  if (!owner || !repo) {
    return null;
  }
  return `https://github.com/${owner}/${repo}`;
}

function notebookPathFromEntry(entry) {
  if (entry.type !== 'Chapter' || !entry.path.includes('/theory.md')) {
    return null;
  }
  return entry.path.replace('content/chapters/', 'chapters/').replace('/theory.md', '/notebook.ipynb');
}

function buildToc(catalog, currentId) {
  const toc = document.getElementById('toc');
  toc.innerHTML = '';
  for (const entry of catalog) {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = `reader.html?id=${encodeURIComponent(entry.id)}`;
    a.textContent = entry.title;
    if (entry.id === currentId) {
      a.classList.add('active');
    }
    li.appendChild(a);
    toc.appendChild(li);
  }
}

function setPrevNext(catalog, index) {
  const prev = document.getElementById('prev-link');
  const next = document.getElementById('next-link');

  if (index > 0) {
    prev.href = `reader.html?id=${encodeURIComponent(catalog[index - 1].id)}`;
    prev.style.visibility = 'visible';
  } else {
    prev.style.visibility = 'hidden';
  }

  if (index < catalog.length - 1) {
    next.href = `reader.html?id=${encodeURIComponent(catalog[index + 1].id)}`;
    next.style.visibility = 'visible';
  } else {
    next.style.visibility = 'hidden';
  }
}

function setNotebookLink(entry) {
  const notebookLink = document.getElementById('notebook-link');
  const repoBase = detectRepoBase();
  const notebookPath = notebookPathFromEntry(entry);

  if (repoBase && notebookPath) {
    const branch = (window.BOOK_CONFIG && window.BOOK_CONFIG.defaultBranch) || 'main';
    notebookLink.href = `${repoBase}/blob/${encodeURIComponent(branch)}/${notebookPath}`;
    notebookLink.style.display = 'inline';
  } else {
    notebookLink.style.display = 'none';
  }
}

async function loadMarkdown(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Could not read ${path}`);
  }
  return response.text();
}

(async () => {
  const content = document.getElementById('markdown-content');
  const title = document.getElementById('doc-title');
  const meta = document.getElementById('doc-meta');
  if (window.setupThemePicker) {
    window.setupThemePicker('theme-picker-reader');
  }

  try {
    const catalog = await loadCatalog();
    const id = queryId() || catalog[0].id;
    const index = catalog.findIndex((item) => item.id === id);
    const selected = index >= 0 ? catalog[index] : catalog[0];

    buildToc(catalog, selected.id);
    setPrevNext(catalog, index >= 0 ? index : 0);
    setNotebookLink(selected);

    title.textContent = selected.title;
    meta.textContent = `${selected.type} | Source: ${selected.path}`;

    const markdown = await loadMarkdown(selected.path);
    content.innerHTML = marked.parse(markdown);
    document.title = `${selected.title} | Book Reader`;
  } catch (error) {
    title.textContent = 'Unable to load page';
    meta.textContent = '';
    content.innerHTML = `<p>${error.message}</p>`;
  }
})();
