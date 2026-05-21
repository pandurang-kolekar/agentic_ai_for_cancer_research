async function loadCatalog() {
  const response = await fetch('catalog.json');
  if (!response.ok) {
    throw new Error('Unable to load catalog.json');
  }
  return response.json();
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

function parseRepoSlug(repoBase) {
  const match = repoBase.match(/^https:\/\/github\.com\/([^/]+)\/([^/]+)$/i);
  if (!match) {
    return null;
  }
  return { owner: match[1], repo: match[2] };
}

function buildNotebookUrl(repoBase, branch, notebookPath) {
  const viewer = (window.BOOK_CONFIG && window.BOOK_CONFIG.notebookViewer) || 'github';
  const slug = parseRepoSlug(repoBase);

  if (slug && viewer === 'nbviewer') {
    return `https://nbviewer.org/github/${slug.owner}/${slug.repo}/blob/${encodeURIComponent(branch)}/${notebookPath}`;
  }
  if (slug && viewer === 'colab') {
    return `https://colab.research.google.com/github/${slug.owner}/${slug.repo}/blob/${encodeURIComponent(branch)}/${notebookPath}`;
  }
  if (slug && viewer === 'raw') {
    return `https://raw.githubusercontent.com/${slug.owner}/${slug.repo}/${encodeURIComponent(branch)}/${notebookPath}`;
  }
  return `${repoBase}/blob/${encodeURIComponent(branch)}/${notebookPath}`;
}

function buildCard(entry, repoBase, index) {
  const a = document.createElement('a');
  a.className = 'card';
  a.href = `reader.html?id=${encodeURIComponent(entry.id)}`;
  a.style.animationDelay = `${Math.min(index * 40, 600)}ms`;

  const tag = document.createElement('div');
  tag.className = 'tag';
  tag.textContent = entry.type;

  const title = document.createElement('h3');
  title.textContent = entry.title;

  const desc = document.createElement('p');
  desc.textContent = entry.description;

  a.appendChild(tag);
  a.appendChild(title);
  a.appendChild(desc);

  const notebookPath = notebookPathFromEntry(entry);
  if (repoBase && notebookPath) {
    const actions = document.createElement('div');
    actions.className = 'card-actions';

    const notebook = document.createElement('a');
    const branch = (window.BOOK_CONFIG && window.BOOK_CONFIG.defaultBranch) || 'main';
    notebook.href = buildNotebookUrl(repoBase, branch, notebookPath);
    notebook.className = 'card-link';
    notebook.target = '_blank';
    notebook.rel = 'noopener noreferrer';
    notebook.textContent = 'Open Notebook';
    notebook.addEventListener('click', (event) => event.stopPropagation());

    actions.appendChild(notebook);
    a.appendChild(actions);
  }

  return a;
}

function filterCatalog(catalog, query) {
  const normalized = query.trim().toLowerCase();
  if (!normalized) {
    return catalog;
  }
  return catalog.filter((entry) => {
    const haystack = `${entry.type} ${entry.title} ${entry.description}`.toLowerCase();
    return haystack.includes(normalized);
  });
}

(async () => {
  const grid = document.getElementById('chapter-grid');
  const searchInput = document.getElementById('catalog-search');
  if (window.setupThemePicker) {
    window.setupThemePicker('theme-picker-home');
  }
  try {
    const catalog = await loadCatalog();
    const repoBase = detectRepoBase();

    function render(query = '') {
      grid.innerHTML = '';
      const filtered = filterCatalog(catalog, query);
      if (filtered.length === 0) {
        grid.innerHTML = '<p>No matches found. Try a broader term.</p>';
        return;
      }
      for (const [index, entry] of filtered.entries()) {
        grid.appendChild(buildCard(entry, repoBase, index));
      }
    }

    render('');
    if (searchInput) {
      searchInput.addEventListener('input', (event) => {
        render(event.target.value);
      });
    }
  } catch (error) {
    grid.innerHTML = `<p>Could not load content catalog: ${error.message}</p>`;
  }
})();
