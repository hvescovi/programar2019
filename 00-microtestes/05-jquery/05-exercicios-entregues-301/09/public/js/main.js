class Game {

    constructor() {
        this.sky_color = 0xdbebfa;
        this.ground_color = 0x63b200;
        this.sun_color = 0xfdb813;
        this.fog_color = 0xdfddd6;
        
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(this.sky_color);
        
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 4096);
        this.camera.aspect = window.innerWidth / window.innerHeight;

        this.canvas = document.getElementById("threejs");
        this.renderer = new THREE.WebGLRenderer({canvas: this.canvas});
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.BasicShadowMap;
        this.renderer.shadowMapCullface = THREE.CullFaceBack;
        this.renderer.gammaInput = true;
        this.renderer.gammaOutput = true;
        
        this.scene.fog = new THREE.Fog(this.fog_color, 0, 20000);
        this.renderer.setClearColor(this.scene.fog.color, 1);
        
        //document.body.appendChild(this.renderer.domElement);

        this.setupStats();
        
        window.addEventListener( 'resize', this.onWindowResize.bind(this), false );

        this.keyboard = new KeyboardState();
        this.setupControls();
        
        this.latency = 0;
        this.time = 0.5;

        this.current_time = performance.now();
        this.last_time = this.current_time;
        this.alpha = 0;

        this.loops = 0;
        this.sim_fps = 64;
        this.skip_ticks = 1000 / this.sim_fps;
        this.max_frame_skip = 10;
        this.next_game_tick = performance.now();
    }

    setupStats(){
        this.stats = new Stats();
        this.up_stats = new Stats();
        function setStatPos(stat, left) {
            stat.domElement.style.position = "absolute";
            stat.domElement.style.left = left + "px";
            stat.domElement.style.top = "0px"
        }
        setStatPos(this.stats, 0);
        setStatPos(this.up_stats, 100);

        //this.up_stats.domElement.style.margin = "0px 0px 0px 80px";
        this.stats.showPanel(1);
        this.up_stats.showPanel(0);

        document.body.appendChild(this.stats.domElement);
        document.body.appendChild(this.up_stats.domElement);
    }
    
    setupControls(){
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
    }

    onWindowResize(){
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();

        this.renderer.setSize( window.innerWidth, window.innerHeight );
    }
    
    createSky(){
        this.sky_vs = document.getElementById("vertexShader").textContent;
        this.sky_vf = document.getElementById("fragmentShader").textContent;
        
        this.sky_uniforms = {
            topColor:    { type: "c", value: new THREE.Color( 0x0077ff ) },
            bottomColor: { type: "c", value: new THREE.Color( 0xffffff ) },
            offset:      { type: "f", value: 33 },
            exponent:    { type: "f", value: 0.6 }
        }
        this.sky_uniforms.topColor.value.copy(this.hemiLight.color);
        
        this.scene.fog.color.copy(this.sky_uniforms.bottomColor.value);
        
        this.sky_geo = new THREE.SphereGeometry(8000, 32, 15);
        this.sky_mat = new THREE.ShaderMaterial( { vertexShader: this.sky_vs, fragmentShader: this.sky_fs, uniforms: this.sky_uniforms, side: THREE.BackSide } );
        
        this.sky = new THREE.Mesh(this.sky_geo, this.sky_mat);
        this.scene.add(this.sky);
    }
    
    createLights(){
        this.hemiLight = new THREE.HemisphereLight(0xffffff, 0xffffff, 0.05);
        this.hemiLight.color.setHSL(0.6, 1, 0.6);
        this.hemiLight.groundColor.setHSL(0.095, 1, 0.75);
        this.scene.add(this.hemiLight);
        
        this.sunLight = new THREE.DirectionalLight(0xffffff, 1);
        this.sunLight.color.setHSL(0.1, 1, 0.95);
        this.sunLight.position.set(-1, 0.75, 1);
        this.sunLight.position.multiplyScalar(50);
        this.scene.add(this.sunLight);
        
        this.sunLight.castShadow = true;
        this.sunLight.shadow.mapSize.width = this.sunLight.shadow.mapSize.height = 1024*2;
        
        this.d = 30;
        this.sunLight.shadow.camera.left = -this.d;
        this.sunLight.shadow.camera.right = this.d;
        this.sunLight.shadow.camera.top = this.d;
        this.sunLight.shadow.camera.bottom = -this.d;
        
        this.sunLight.shadow.camera.Far = 3500;
        this.sunLight.shadow.bias = -0.000001;
        this.sunLight.shadow.darkness = 0.35;
        this.scene.add(this.sunLight);
    }
    
    createTerrain(){
        var generateHeight = function( width, height ) {
            
            var size = width * height, 
                z = Math.random() * 100;
            
            var data = new Uint8Array(size);
            var perlin = new ImprovedNoise();
            var quality = 2;
            for (var j=0; j<4; j++){
                quality *= 2;
                for (var i=0; i < size; i++){
                    var x = i % width,
                        y = ~~ (i / height);

                    var nx = x/quality - 0.5,
                        ny = y/quality - 0.5;
                    data[i] += perlin.noise(nx, ny, z) * quality + 10;

                }
            }
            return data;
        }        
        
        var data = generateHeight(1024, 1024);

        //var image_data = new THREE.TextureLoader().load("test.png");
        var material = new THREE.MeshLambertMaterial({color: this.ground_color, wireframe: false}); // color: this.ground_color
        material.flatShading = true;
        
        var quality = 16,
            step = 1024 / quality;
        
        var geometry = new THREE.PlaneGeometry(2000, 2000, quality -1, quality -1);
        geometry.dynamic = true;
        geometry.rotateX(- Math.PI / 2);
        
        for (var i=0, l=geometry.vertices.length; i < l; i++){
            var x = i % quality,
                y = Math.floor(i / quality);
            geometry.vertices[i].y = data[(x*step)+(y*step)*1024] * 2 - 128;
        }
        
        //geometry.computeFlatVertexNormals();
        this.terrainMesh = new THREE.Mesh(geometry, material);
        this.terrainMesh.castShadow = true;
        this.scene.add(this.terrainMesh);
    }

    init() {
        this.createTerrain();        
        this.createLights();
        this.createSky();

        
        this.camera.position.y = 512;
        /*
        this.camera.position.y = 768;
        this.camera.position.z = 512;
        this.camera.lookAt(0, 0, 0);
        */

        this.setup_network("localhost");

        this.current_time = performance.now();
    }
    
    latency_update(ms){
        this.latency = ms;
        this.socket.emit("ping_back", {ping: ms});
    }
    
    setup_network(ip = "localhost", port = "3000"){
        this.socket = io.connect("http://"+ip+":"+port);
        this.socket.on("pong", this.latency_update.bind(this));
    }

    updateSun(delta){
        var nsin = Math.sin(delta);
        var ncos = Math.cos(delta);
        
        this.sunLight.position.set( 1500*nsin, 2000*nsin, 2000*ncos);
        this.terrainMesh.geometry.computeFlatVertexNormals();
        if (nsin > 0.2 )   // day
        {
            this.sky.material.uniforms.topColor.value.setRGB(0.25,0.55,1);
            this.sky.material.uniforms.bottomColor.value.setRGB(1,1,1);
            var f = 1;
            this.sunLight.intensity = f;
            this.sunLight.shadow.darkness = f*0.7;
        }
        else if (nsin < 0.2 && nsin > 0.0 )
        {
            var f = nsin/0.2;
            this.sunLight.intensity = f;
            this.sunLight.shadow.darkness = f*0.7;
            this.sky.material.uniforms.topColor.value.setRGB(0.25*f,0.55*f,1*f);
            this.sky.material.uniforms.bottomColor.value.setRGB(1*f,   1*f,1*f);
        }
        else  // night
        {
            var f = 0;
            this.sunLight.intensity = f;
            this.sunLight.shadow.darkness = f*0.7;
            this.sky.material.uniforms.topColor.value.setRGB(0,0,0);
            this.sky.material.uniforms.bottomColor.value.setRGB(0,0,0);
        }
    }
    
    handle_input() {
        this.keyboard.update();
    }

    gameTick() {
        //this.controls.update();
        //this.time += (0.1/1000)*this.skip_ticks;
        if (this.time >= 4)
            this.time = 0;
        
        this.updateSun(this.time);
    }

    draw() {
        this.renderer.render(this.scene, this.camera);
    }

    run() {
        requestAnimationFrame(this.run.bind(this));
        this.last_time = this.current_time;
        this.current_time = performance.now();
        this.delta = this.current_time - this.last_time;

        this.handle_input();

        this.loops = 0;

        while (this.current_time > this.next_game_tick && this.loops < this.max_frame_skip) {
            this.up_stats.update();
            this.loops++;
            this.gameTick();
            this.next_game_tick += this.skip_ticks;
        }

        this.draw();

        //monitor performance
        this.stats.update();
    }
}

var game = new Game();
game.init();

game.run();