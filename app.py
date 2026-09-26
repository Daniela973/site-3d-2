import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PrimeTech Solutions | Sistemas e Automações",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PrimeTech Solutions - Tecnologia e Automação</title>
    <!-- Three.js para o setup 3D completo -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        :root {
            --bg-deep: #05050a;
            --bg-card: rgba(16, 16, 26, 0.85);
            --bg-card-hover: rgba(22, 22, 36, 0.95);
            --accent-cyan: #00f2fe;
            --accent-blue: #4facfe;
            --accent-purple: #7f00ff;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
        }

        * { box-sizing: border-box; scroll-behavior: smooth; }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            overflow-x: hidden;
        }

        #bg-canvas {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            pointer-events: none;
        }

        header {
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(5, 5, 10, 0.85);
            backdrop-filter: blur(15px);
            border-bottom: 1px solid rgba(255,255,255,0.08);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.4rem;
            font-weight: 800;
            color: #fff;
        }
        .logo span { color: var(--accent-cyan); }

        nav {
            display: flex;
            gap: 1.2rem;
            align-items: center;
        }

        nav a {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
            transition: color 0.2s;
        }
        nav a:hover { color: var(--accent-cyan); }

        .btn-header {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.4rem 1rem;
            border-radius: 6px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.8rem;
        }

        .hero {
            padding: 3rem 5% 2rem 5%;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        #canvas-container {
            width: 100%;
            height: 380px;
            margin: 1rem auto;
            cursor: grab;
        }
        #canvas-container:active { cursor: grabbing; }

        .hero h1 {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            color: #fff;
            letter-spacing: -1px;
        }

        .hero h1 span {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.1rem;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }

        .cta-btn {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.8rem 2rem;
            font-size: 0.95rem;
            font-weight: 800;
            border-radius: 8px;
            text-decoration: none;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.35);
            display: inline-block;
            transition: transform 0.2s;
        }
        .cta-btn:hover { transform: translateY(-2px); }

        .section {
            padding: 4rem 5%;
            max-width: 1000px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        .section-title {
            font-size: 1.8rem;
            margin-bottom: 2.5rem;
            text-align: center;
            color: #fff;
            font-weight: 800;
        }

        .floating-box {
            background: var(--bg-card);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 16px;
            padding: 2.5rem 1.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
            animation: floatSlow 6s ease-in-out infinite;
        }

        @keyframes floatSlow {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }

        .flow-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
        }
        .flow-card {
            background: var(--bg-card);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 1.8rem;
            transition: transform 0.3s, border-color 0.3s;
        }
        .flow-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent-cyan);
        }
        .flow-card h4 { color: #fff; margin-top: 0; font-size: 1.1rem; margin-bottom: 0.8rem; }
        .flow-card p { color: var(--text-muted); margin: 0; font-size: 0.95rem; }

        .services-stack {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
        }
        .service-item {
            background: var(--bg-card);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 1.2rem 1.8rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s;
        }
        .service-item:hover {
            border-color: var(--accent-cyan);
            background: var(--bg-card-hover);
            transform: scale(1.01);
        }
        .service-item h4 { color: #fff; margin: 0; font-size: 1rem; font-weight: 600; }
        .service-item span { color: var(--accent-cyan); font-size: 0.75rem; font-weight: 600; background: rgba(0,242,254,0.1); padding: 0.3rem 0.7rem; border-radius: 6px; }

        .diff-steps {
            display: flex;
            justify-content: center;
            gap: 0.8rem;
            flex-wrap: wrap;
            margin-top: 1.5rem;
        }
        .diff-step-pill {
            background: rgba(127, 0, 255, 0.25);
            border: 1px solid rgba(127, 0, 255, 0.6);
            color: #fff;
            padding: 0.6rem 1.1rem;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 700;
            box-shadow: 0 0 15px rgba(127, 0, 255, 0.3);
        }

        .whatsapp-float {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: #25d366;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 4px 20px rgba(37, 211, 102, 0.5);
            z-index: 1000;
            text-decoration: none;
            transition: transform 0.3s;
        }
        .whatsapp-float:hover { transform: scale(1.1); }

        footer {
            text-align: center;
            padding: 3rem 5%;
            color: var(--text-muted);
            border-top: 1px solid rgba(255,255,255,0.05);
            font-size: 0.85rem;
            position: relative;
            z-index: 2;
        }
    </style>
</head>
<body>

    <canvas id="bg-canvas"></canvas>

    <header>
        <div class="logo">Prime<span>Tech</span></div>
        <nav>
            <a href="#problema">O Problema</a>
            <a href="#solucao">Transformação</a>
            <a href="#servicos">Serviços</a>
            <a href="#diferencial">Diferencial</a>
        </nav>
        <a href="https://wa.me/5511999999999?text=Olá,%20gostaria%20de%20conversar%20sobre%20automações." target="_blank" class="btn-header">Falar com Especialista</a>
    </header>

    <!-- 1️⃣ HERO COM SETUP DE COMPUTADOR COMPLETO + MOUSE + COMPONENTES 3D -->
    <section class="hero">
        <h1>Sua empresa ainda perde tempo com <span>processos manuais</span>?</h1>
        <p>A PrimeTech Solutions transforma tarefas repetitivas em sistemas e automações inteligentes que geram eficiência real para o seu negócio.</p>
        
        <div id="canvas-container"></div>

        <div style="margin-top: 1rem;">
            <a href="https://wa.me/5511999999999?text=Olá,%20quero%20conhecer%20as%20soluções%20da%20PrimeTech." target="_blank" class="cta-btn">Conheça nossas soluções</a>
        </div>
    </section>

    <!-- 2️⃣ O PROBLEMA -->
    <section id="problema" class="section">
        <h2 class="section-title">O caos operacional diário</h2>
        <div class="flow-grid">
            <div class="flow-card">
                <h4>📄 Planilhas e Documentos</h4>
                <p>Dados descentralizados, arquivos pesados e informações perdidas entre equipes.</p>
            </div>
            <div class="flow-card">
                <h4>📧 E-mails e WhatsApp</h4>
                <p>Atendimento manual repetitivo, falta de histórico e atrasos nas respostas.</p>
            </div>
            <div class="flow-card">
                <h4>👨‍💼 Trabalho Manual</h4>
                <p>Horários desperdiçados em cadastros e relatórios que poderiam ser automatizados.</p>
            </div>
        </div>
    </section>

    <!-- 3️⃣ A TRANSFORMAÇÃO -->
    <section id="solucao" class="section">
        <h2 class="section-title">Do caos à automação inteligente</h2>
        <div class="floating-box" style="text-align: center;">
            <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 1.1rem; font-weight: 600;">Como organizamos e escalamos a sua operação corporativa:</p>
            <div class="diff-steps">
                <span class="diff-step-pill">1. CLIENTES</span>
                <span style="color: var(--accent-cyan); align-self: center; font-weight: bold;">→</span>
                <span class="diff-step-pill">2. AUTOMAÇÃO</span>
                <span style="color: var(--accent-cyan); align-self: center; font-weight: bold;">→</span>
                <span class="diff-step-pill">3. DADOS SEGUROS</span>
                <span style="color: var(--accent-cyan); align-self: center; font-weight: bold;">→</span>
                <span class="diff-step-pill">4. RESULTADOS</span>
            </div>
        </div>
    </section>

    <!-- 4️⃣ SERVIÇOS -->
    <section id="servicos" class="section">
        <h2 class="section-title">O que desenvolvemos para sua empresa</h2>
        <div class="services-stack">
            <div class="service-item">
                <h4>01 — Desenvolvimento de Sistemas</h4>
                <span>Python + Gestão + CRUD</span>
            </div>
            <div class="service-item">
                <h4>02 — Automação de Processos</h4>
                <span>Python + Tarefas Repetitivas</span>
            </div>
            <div class="service-item">
                <h4>03 — Integração de APIs</h4>
                <span>Conectando suas Ferramentas</span>
            </div>
            <div class="service-item">
                <h4>04 — Sistemas de Gestão</h4>
                <span>Controle Operacional Completo</span>
            </div>
            <div class="service-item">
                <h4>05 — Soluções para Empresas</h4>
                <span>Infraestrutura e Otimização</span>
            </div>
            <div class="service-item">
                <h4>06 — Segurança e Proteção de Dados</h4>
                <span>Armazenamento Confiável</span>
            </div>
        </div>
    </section>

    <!-- 5️⃣ SEU DIFERENCIAL -->
    <section id="diferencial" class="section">
        <h2 class="section-title">Nosso Diferencial Tecnológico</h2>
        <div class="floating-box" style="text-align: center;">
            <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 1.05rem;">Unimos conhecimento profundo de infraestrutura, arquitetura de sistemas e software para entregar valor ponta a ponta:</p>
            <div class="diff-steps">
                <span class="diff-step-pill">Hardware</span>
                <span style="color: var(--accent-cyan);">↓</span>
                <span class="diff-step-pill">Sistema</span>
                <span style="color: var(--accent-cyan);">↓</span>
                <span class="diff-step-pill">Banco de Dados</span>
                <span style="color: var(--accent-cyan);">↓</span>
                <span class="diff-step-pill">APIs</span>
                <span style="color: var(--accent-cyan);">↓</span>
                <span class="diff-step-pill">Solução Completa</span>
            </div>
        </div>
    </section>

    <!-- CONTATO / CTA FINAL -->
    <section class="hero" style="padding-top: 1rem;">
        <h2 class="section-title">Pronto para transformar sua empresa?</h2>
        <p>Fale diretamente com nossa equipe e descubra como otimizar seus processos ainda esta semana.</p>
        <a href="https://wa.me/5511999999999?text=Olá,%20quero%20conversar%20sobre%20um%20projeto%20para%20minha%20empresa." target="_blank" class="cta-btn" style="font-size: 1.1rem; padding: 1rem 2.5rem;">💬 Falar no WhatsApp agora</a>
    </section>

    <a href="https://wa.me/5511999999999?text=Olá,%20gostaria%20de%20saber%20mais%20sobre%20as%20soluções%20da%20PrimeTech." target="_blank" class="whatsapp-float" title="Falar no WhatsApp">
        💬
    </a>

    <footer>
        <p>&copy; 2026 PrimeTech Solutions. Todos os direitos reservados.</p>
    </footer>

    <!-- Script 3D: Setup Completo de Computador (Monitor Brilhante, Teclado, Mouse e Partículas de Luz) -->
    <script>
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        // Grupo principal do Setup do Computador
        const pcGroup = new THREE.Group();

        // 1. Base / Mesa digitalizadora ou suporte inferior
        const deskBaseGeo = new THREE.BoxGeometry(4.2, 0.1, 2.6);
        const deskBaseMat = new THREE.MeshStandardMaterial({ color: 0x1f1f32, roughness: 0.4, metalness: 0.7 });
        const deskBase = new THREE.Mesh(deskBaseGeo, deskBaseMat);
        deskBase.position.y = -0.6;
        pcGroup.add(deskBase);

        // 2. Monitor / Computador Completo (Tela com alto brilho e moldura clara)
        const monitorGeo = new THREE.BoxGeometry(3.4, 2.1, 0.15);
        const monitorMat = new THREE.MeshStandardMaterial({ color: 0x2b2b45, roughness: 0.2, metalness: 0.8 });
        const monitor = new THREE.Mesh(monitorGeo, monitorMat);
        monitor.position.set(0, 0.5, 0);
        pcGroup.add(monitor);

        // Display brilhante e colorido (Com elementos e código simulado visíveis)
        const displayGeo = new THREE.BoxGeometry(3.1, 1.8, 0.05);
        const displayMat = new THREE.MeshBasicMaterial({ color: 0x00f2fe });
        const display = new THREE.Mesh(displayGeo, displayMat);
        display.position.set(0, 0.5, 0.09);
        pcGroup.add(display);

        // Hastes de suporte do monitor
        const standGeo = new THREE.BoxGeometry(0.4, 0.6, 0.4);
        const standMat = new THREE.MeshStandardMaterial({ color: 0x3d3d5c, metalness: 0.9 });
        const stand = new THREE.Mesh(standGeo, standMat);
        stand.position.set(0, -0.35, 0);
        pcGroup.add(stand);

        // 3. Teclado 3D na frente do monitor
        const keyboardGeo = new THREE.BoxGeometry(2.6, 0.08, 1.0);
        const keyboardMat = new THREE.MeshStandardMaterial({ color: 0x22223b, roughness: 0.5, metalness: 0.6 });
        const keyboard = new THREE.Mesh(keyboardGeo, keyboardMat);
        keyboard.position.set(0, -0.5, 1.0);
        pcGroup.add(keyboard);

        // 4. Mouse 3D ao lado do teclado
        const mouseGeo = new THREE.BoxGeometry(0.4, 0.12, 0.7);
        const mouseMat = new THREE.MeshStandardMaterial({ color: 0x00f2fe, roughness: 0.3, metalness: 0.8 });
        const mouse = new THREE.Mesh(mouseGeo, mouseMat);
        mouse.position.set(1.8, -0.5, 0.9);
        pcGroup.add(mouse);

        scene.add(pcGroup);

        // 5. Partículas de Luz e Dados (Flutuando ao redor do computador)
        const particleCount = 80;
        const particleGeo = new THREE.BufferGeometry();
        const particlePositions = new Float32Array(particleCount * 3);

        for (let i = 0; i < particleCount * 3; i += 3) {
            particlePositions[i] = (Math.random() - 0.5) * 7;
            particlePositions[i + 1] = (Math.random() - 0.5) * 5;
            particlePositions[i + 2] = (Math.random() - 0.5) * 7;
        }

        particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
        const particleMat = new THREE.PointsMaterial({
            color: 0x00f2fe,
            size: 0.08,
            transparent: true,
            opacity: 0.9
        });
        const particles = new THREE.Points(particleGeo, particleMat);
        scene.add(particles);

        // Iluminação Forte e Colorida para destacar o Computador
        scene.add(new THREE.AmbientLight(0xffffff, 1.2));
        const frontLight = new THREE.PointLight(0x00f2fe, 4, 30);
        frontLight.position.set(0, 2, 4);
        scene.add(frontLight);

        const purpleLight = new THREE.PointLight(0x7f00ff, 3, 30);
        purpleLight.position.set(-3, -2, 3);
        scene.add(purpleLight);

        camera.position.z = 5.2;

        // Controles de Arraste por Mouse / Toque
        let isDragging = false;
        let prevMousePos = { x: 0, y: 0 };

        container.addEventListener('mousedown', (e) => { isDragging = true; prevMousePos = { x: e.clientX, y: e.clientY }; });
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            pcGroup.rotation.y += (e.clientX - prevMousePos.x) * 0.01;
            pcGroup.rotation.x += (e.clientY - prevMousePos.y) * 0.01;
            prevMousePos = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => { isDragging = false; });

        container.addEventListener('touchstart', (e) => { isDragging = true; prevMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY }; });
        window.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            pcGroup.rotation.y += (e.touches[0].clientX - prevMousePos.x) * 0.01;
            pcGroup.rotation.x += (e.touches[0].clientY - prevMousePos.y) * 0.01;
            prevMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        });
        window.addEventListener('touchend', () => { isDragging = false; });

        // Fundo 3D Global com formas geométricas espalhadas
        const bgCanvas = document.getElementById('bg-canvas');
        const bgScene = new THREE.Scene();
        const bgCamera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
        const bgRenderer = new THREE.WebGLRenderer({ canvas: bgCanvas, alpha: true, antialias: true });
        bgRenderer.setSize(window.innerWidth, window.innerHeight);
        bgCamera.position.z = 10;

        const floatingObjects = [];
        const geometries = [
            new THREE.BoxGeometry(0.9, 0.9, 0.9),
            new THREE.OctahedronGeometry(0.8),
            new THREE.TetrahedronGeometry(0.9)
        ];

        for (let i = 0; i < 18; i++) {
            const geo = geometries[Math.floor(Math.random() * geometries.length)];
            const mat = new THREE.MeshStandardMaterial({
                color: i % 2 === 0 ? 0x00f2fe : 0x7f00ff,
                wireframe: true,
                transparent: true,
                opacity: 0.4
            });
            const mesh = new THREE.Mesh(geo, mat);
            mesh.position.set(
                (Math.random() - 0.5) * 18,
                (Math.random() - 0.5) * 28,
                (Math.random() - 0.5) * 12
            );
            bgScene.add(mesh);
            floatingObjects.push(mesh);
        }

        bgScene.add(new THREE.AmbientLight(0xffffff, 0.9));

        // Loop de Animação com Partículas e Reação ao Scroll
        function animate() {
            requestAnimationFrame(animate);

            if (!isDragging) {
                pcGroup.rotation.y += 0.003;
                pcGroup.rotation.x = Math.sin(Date.now() * 0.001) * 0.1;
            }

            // Movimento das partículas de dados de luz
            const positions = particleGeo.attributes.position.array;
            for (let i = 1; i < positions.length; i += 3) {
                positions[i] -= 0.01;
                if (positions[i] < -3) positions[i] = 3;
            }
            particleGeo.attributes.position.needsUpdate = true;

            // Reação ao scroll da página
            const scrollY = window.scrollY;
            pcGroup.position.y = scrollY * 0.0008;

            floatingObjects.forEach((obj, index) => {
                obj.rotation.x += 0.004 + (index * 0.0004);
                obj.rotation.y += 0.006 + (index * 0.0004);
            });

            bgRenderer.render(bgScene, bgCamera);
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);

            bgCamera.aspect = window.innerWidth / window.innerHeight;
            bgCamera.updateProjectionMatrix();
            bgRenderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>
"""

components.html(html_code, height=2700, scrolling=True)
