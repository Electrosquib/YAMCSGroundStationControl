<pre>
trxvu_yamcs/
├─ .github/
├─ .mvn/
│  └─ wrapper/
│     └─ maven-wrapper.properties
├─ docker/
│  ├─ docker-compose.yml
│  ├─ Dockerfile
│  ├─ Makefile
│  └─ README.md
├─ src/
│  └─ main/
│     ├─ java/
│     │  └─ com/
│     │     └─ example/
│     │        └─ myproject/
│     │           ├─ MyCommandPostprocessor.java
│     │           └─ MyPacketPreprocessor.java
│     └─ yamcs/
│        ├─ etc/
│        │  ├─ **ground_control.yaml**
│        │  ├─ processor.yaml
│        │  ├─ yamcs.myproject.yaml
│        │  └─ yamcs.yaml
│        └─ mdb/
│           └─ xtce.xml
├─ target/
│  ├─ classes/
│  │  └─ com/
│  │     └─ example/
│  │        └─ myproject/
│  │           ├─ MyCommandPostprocessor.class
│  │           └─ MyPacketPreprocessor.class
│  ├─ generated-sources/
│  │  └─ annotations/
│  ├─ maven-status/
│  │  └─ maven-compiler-plugin/
│  │     └─ compile/
│  │        └─ default-compile/
│  │           ├─ createdFiles.lst
│  │           └─ inputFiles.lst
│  ├─ test-classes/
│  └─ yamcs/
│     ├─ cache/
│     │  ├─ yamcs-web/
│     │  │  ├─ icons/
│     │  │  │  ├─ icon-192x192.png
│     │  │  │  ├─ icon-512x512.png
│     │  │  │  └─ icon-96x96.png
│     │  │  ├─ media/
                ...
│     │  │  ├─ ...
│     │  ├─ 93ECFDDBE677289EF138493C9328A9CA397D4BC1.consistency_date
│     │  └─ 93ECFDDBE677289EF138493C9328A9CA397D4BC1.serialized
│     ├─ etc/
│     │  ├─ **ground_control.yaml**
│     │  ├─ processor.yaml
│     │  ├─ **yamcs.ground_control.yaml**
│     │  ├─ yamcs.myproject.yaml
│     │  └─ yamcs.yaml
│     ├─ mdb/
│     │  └─ xtce.xml
│     └─ yamcs-data/
│        ├─ _global/
│        ├─ _global.rdb/
│        │  ├─ ...
│        ├─ ground_control.rdb/ **(Automatically Generated)**
│        │  ├─ CURRENT
│        │  ├─ IDENTITY
│        │  ├─ LOCK
│        │  ├─ LOG
│        │  ├─ MANIFEST-000005
│        │  ├─ OPTIONS-000009
│        │  └─ OPTIONS-000011
│        ├─ instance-def/
│        └─ myproject.rdb/
│           └─ ...
├─ workflows/
│  └─ main.yml
├─ .gitignore
├─ mvnw
├─ mvnw.cmd
├─ pom.xml
├─ README.md
├─ simulator.py
└─ testdata.ccsds
</pre>
