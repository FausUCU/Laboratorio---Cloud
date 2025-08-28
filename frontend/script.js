// URLs de tus Functions
const getNewsUrl = "https://getnewsfunc-hgbgehfubxgbhyep.brazilsouth-01.azurewebsites.net/api/GetNews?code=7RE8KtCmEFWnMmouUCikvWBITygrV8rzZYoopyhQwNDnAzFuiUAcfw==";
const logAccessUrl = "https://logaccessfunc-abg3f8aycthuhaa2.brazilsouth-01.azurewebsites.net/api/LogAccess";

// Función para cargar titulares
async function loadNews(country, category) {
  try {
    // 1. Llamada a GetNews con parámetros
    const url = `${getNewsUrl}&country=${country}&category=${category}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error("Error en GetNews");

    const news = await res.json();

    // 2. Mostrar titulares en la lista
    const list = document.getElementById("newsList");
    list.innerHTML = "";

    news.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item.title; // GetNews devuelve { title }
      list.appendChild(li);
    });

    // 3. Registrar acceso en LogAccess
    await fetch(logAccessUrl, { method: "POST" });

  } catch (err) {
    console.error("Error cargando noticias:", err);
    alert("No se pudieron cargar las noticias.");
  }
}

// Captura el submit del formulario
document.getElementById("filterForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const country = document.getElementById("country").value;
  const category = document.getElementById("category").value;
  loadNews(country, category);
});

// Cargar titulares automáticamente al iniciar la página
window.onload = () => loadNews("us", "general");
