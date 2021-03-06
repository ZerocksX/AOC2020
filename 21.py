from __future__ import print_function

inp = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

inp = """zgdllp fkjmz hnkbr dmthbf flp ptzxb ndvrq ldlpqdx kjkrm vhgjx xhhp kxjttzg nsjzj xlqvs bfgktfm jrk chnnns rrqrbt mmrjb gtbhdgf rzhxzk bdnqhn vsp ggjk cbslk xcsdtgb clkcq nnbsm qrbql zctt ggzqx rmrg ldm ssdp sqbdlq lsfktq zjmdst mnzbc ckgd fdcgjhm lnt qzvhx zfhgv jcsksnf rhq tgtkk (contains fish, nuts, sesame)
rhzk xnjn jhhp kxgtgt hrvcn slhsqs gdg fdcgjhm czjnmn zctt mfdrqvg rrqrbt gpqcmc sjmf jxfs nsjzj rnmbgpv hgmt bjksj vjjtq gjrlc frskl qrvq lnd dxd vpkrmfl fqfm znkth jrk sjcnnc hqvn ldm cvts xgjl xmm xxkz rvjpb clkcq ljkdmhpn hscsj ndvrq jlszf rbrhg qzvhx zjmdst ndbq crd lgcdpd qmmf fkjmz qmkhfq qctkc zpxcdt npn jlck gpskmh sqbdlq dlkpcfz kx zmmtvm zmvhck lkzkq kxjttzg pjsmxzmq gtdvh nvnqk rcp trhm shmpchr nnbsm dtfj lmrkv fhs fxmn lksfxx kjkrm zgdllp qzbb nbtvmr jvhp lscp tvsj rbrmc vbtxrg bstzz qrz (contains sesame)
sbpm slhsqs frskl hjsl ndbq rhzk zjmdst qktlffz ndvrq nvnqk ttmfnxn nnbsm dmzrd gtdvh rclhlfv nqpds vjjtq fqfm lgcdpd czjnmn zgdllp tjfp nqmt rvjpb gpqcmc lnt lnd pzns bjsvt kjkrm lsfktq sqbdlq jdlx vbtxrg jgkhfz gjrlc zmmtvm bxtkrc fvqmjm djxff ldm tnsmf xmm jdtdbj cvts ljkdmhpn dsvqv xgjl dlkpcfz tgtkk clkcq lscp xhhp kxjttzg ftzd gdg qrvq vhgjx zctt ckgd mfdrqvg rzmb mnzbc dtfj dkjlhx qctkc mmcff (contains peanuts, wheat, fish)
nvnqk lkzkq rhzk bdnqhn brtrhg xgjl mkjjr czjnmn dmthbf zmmtvm qzvhx brkpckn fkjmz vrsnfl zshknhl stsktc mnzbc hgmt xxkz ldlpqdx spqs xmm zctt cbslk qrbql bhkrr ndvrq fqfm sjcnnc grqppvx sqbdlq glpjxr rrqrbt rltdnr rmrg pjsmxzmq lnd bjksj hlqmb ldm zpxcdt xlqvs jtm ssk kxjttzg zgdllp qctkc gtgtrc ptzxb qktlffz zjzjcx hqvn qmkhfq fdcgjhm vhgjx zjmdst rvjpb (contains dairy, fish)
gtgtrc kxjttzg xnjn kx frskl mfdrqvg hlqmb jgkhfz hqvn flp djxff qctkc rdgp hbzlk ldlpqdx ldm rnmbgpv dkjlhx qcggn kjkrm tnsmf vbtxrg rrqrbt ndvrq dktgnm jlszf cbslk dlkpcfz dkh cgdjss fqfm mnzbc hscsj flkmb krdxd ttmfnxn xxkz lnt rk zctt kxgtgt pjsmxzmq vhgjx gtdvh qmmf rzhxzk rclhlfv qrvq jxfs qmkhfq rqdggr ggjk nnbsm thlvnb fdgf hjsl bfgktfm nqmt fkjmz hscj zpxcdt (contains wheat, sesame, nuts)
lpcjbk lscp xxkz fdcgjhm nzcz nsjzj qkmst qrvq hqvn dmthbf lpgg sjcnnc ftzd fqlmnc hscj nvnqk hjsl zfrg zjzjcx ldm vpkrmfl pjsmxzmq lksfxx fqfm ggzqx xcsdtgb stsktc qrz dkh flkmb vsp rhzk clkcq thlvnb ttmfnxn mfdrqvg ndvrq dlmkn fhs jgkhfz fkjmz zgdllp rbrmc flp qmmf zjmdst chnnns bjqzq mnzbc tnsmf xlqvs vhgjx qzbb grqppvx sjmf lnt kxjttzg zmvhck vbtxrg jdtdbj bhkrr krdxd dxd tgtkk pzns dmzrd ssk ftzmnzv (contains fish, sesame, shellfish)
fqfm fvdgnsr rbrmc mnzbc dkjlhx zfrg gtdvh ndvrq qrbql sdgttdh rhq hqvn fxmn frskl kxjttzg znkth jkttx djlcbd vrsnfl gfxdfvf dlkpcfz zctt brkpckn ftzd zjzjcx xgjl zmvhck kxgtgt bjsvt hrvcn lhxr ldm ggjhzzd zzbvjz flkmb fvqmjm cbslk mczhpbs lnd kjkrm gtbhdgf rqdggr tjfp hnkbr dkh rnmbgpv fdgf jlck cvts zjmdst dlmkn jvhp fdcgjhm npn hbzlk dmthbf lsfktq bdnqhn (contains sesame, dairy)
ndbq ldm nnbsm fvdgnsr rvjpb ssdp mmrjb tjfp rzmb kjkrm fqfm ldlpqdx lfrnc fdgf ndvrq flkmb jspbd jrk stsktc bhkrr bxtkrc bfgktfm zzbvjz pjsmxzmq gjrlc rqdggr zpxcdt vjjtq rhpc qrbql ggjk trhm vpkrmfl cgdjss zjmdst ggjhzzd zgdllp jlszf ftzd tnsmf dktgnm dlmkn fvqmjm jkttx nzcz vrsnfl zjzjcx kxjttzg qmkhfq rmrg ggzqx lnt nqpds ljkdmhpn mnzbc jzfdv shmpchr mfdrqvg xgjl spqs qkmst rhq frskl rnmbgpv zfrg dxd thlvnb xxkz jhhp nbtvmr jlck xvqxszc lmrkv dkjlhx fxmn jvhp (contains eggs)
fkjmz kxjttzg ldm zjmdst lsfktq dlkpcfz xmm qrvq zfrg djxff rhpc stsktc cbslk thlvnb jhhp ndvrq jkttx cgdjss fhs jspbd mnzbc bstzz ldlpqdx zjzjcx krdxd fqfm hrvcn rclhlfv nqmt crtpbnp brtrhg mmcff dkh rdgp tvsj grqppvx dktgnm ckgd ftzmnzv vjjtq lpgg gtbhdgf dxd jlck lkzkq fvdgnsr rmrg hbzlk fdgf dkjlhx qrz (contains sesame, shellfish, nuts)
fvqmjm ftzmnzv mfdrqvg crd hgmt qrz czjnmn zjmdst nbtvmr gpskmh xvqxszc jspbd lsfktq jxfs brtrhg dlkpcfz zfrg flkmb dxd xlqvs qzvhx xhhp mczhpbs ggjk dlmkn rhq rcp grqppvx qmkhfq kjkrm zmmtvm kxjttzg qzbb fkjmz ldm kxpv jlszf gfxdfvf cgdjss hql bdnqhn mnzbc vbtxrg rclhlfv qmmf bjqzq lkzkq lpcjbk lhxr frskl nvnqk fxmn lnt ndvrq sjmf rzhxzk qcggn sjcnnc rdgp nqpds gtbhdgf jdlx hjsl vjjtq chnnns (contains wheat, fish)
gpqcmc rzmb jrk qmkhfq nvnqk slhsqs lkzkq kxpv qkmst dxd fhs hjsl pjsmxzmq rbrmc ttmfnxn qzbb vbtxrg mkjjr sqbdlq zmmtvm ftzd kjkrm gdg dtfj ggzqx jdtdbj hqvn tjfp xssj djxff zjmdst rclhlfv rdgp bjqzq fdcgjhm jlszf sbpm sjcnnc rfgknb mnzbc xxkz lfrnc fdgf ssdp ftzmnzv fkjmz xgjl mmrjb vrsnfl trhm ldm thlvnb flp tvsj hlqmb hql dmthbf zmvhck lksfxx rbrhg xlqvs vsp kxjttzg stlgtj bjksj sphnq bfgktfm kx rqdggr jgkhfz vpkrmfl znkth rrqrbt lnt ckgd jzfdv hrvcn qzvhx xcsdtgb npn frskl gpskmh kxgtgt lpgg cgdjss rhq lmrkv ggjk xnjn lhxr rzhxzk czjnmn ndvrq rhzk hscsj (contains eggs, sesame)
jdtdbj hgmt tgtkk rk dsvqv clkcq ssdp rclhlfv dlmkn ljkdmhpn crtpbnp ndvrq ftzd zmmtvm gjrlc gtgtrc nzcz sjcnnc qrvq rhpc djxff shmpchr ldm nnbsm fxmn sphnq kxgtgt nqmt rhq bhkrr kjkrm rmrg lscp djlcbd hscsj jdlx fqfm lsfktq gpskmh rdgp lksfxx vrsnfl jgkhfz gtbhdgf glpjxr xmm zjmdst mmcff znkth qrz dmthbf fvdgnsr crd frskl vbtxrg ggjk fkjmz mnzbc hnkbr rbrhg jvhp hrvcn jhhp dmzrd (contains wheat)
fvqmjm ndvrq ckgd bxtkrc hlqmb cnkh dtfj ldlpqdx kjkrm gpqcmc rzmb xxkz nsjzj fvdgnsr kxjttzg gtbhdgf nzcz kx jlszf qctkc qcggn ssk xcsdtgb zshknhl dmzrd jxfs npn zmvhck ptzxb fkjmz nvnqk sbpm cgdjss cvts sqbdlq rrqrbt djlcbd cbslk sdgttdh lgcdpd jcsksnf jrk gtgtrc shmpchr stlgtj fdcgjhm dkh bdnqhn bjqzq zgdllp lksfxx kxpv fxmn fqlmnc zctt jspbd qzvhx mnzbc mmcff bfgktfm qrbql lpgg ggzqx dktgnm xvqxszc tnsmf ldm sphnq qmkhfq zjmdst rnmbgpv hjsl czjnmn stsktc (contains fish, wheat)
jkttx sphnq zfrg glpjxr flp dlkpcfz jspbd qrbql dsvqv ljkdmhpn frskl xmm hrvcn djlcbd kjkrm ggzqx clkcq rvjpb bfgktfm fvqmjm hscsj xxkz vsp bjsvt qzbb kx bjqzq ndbq ptzxb zjmdst rclhlfv nbtvmr dkh fxmn nsjzj tvsj gfxdfvf jlck zfhgv flkmb qzvhx jvhp ndvrq fdcgjhm fqfm hnkbr qctkc vrsnfl crd rqdggr kxjttzg mnzbc fkjmz rzmb xvqxszc rmrg lksfxx nqpds lkzkq qmmf zctt nzcz grqppvx cnkh nvnqk sbpm xcsdtgb kxpv jrk mkjjr dmzrd shmpchr ckgd jgkhfz hscj pjsmxzmq jcsksnf rbrmc lnd xgjl sdgttdh (contains nuts)
tjfp fdgf vhgjx spqs chnnns djxff jspbd jhhp lkzkq rdgp xssj rnmbgpv hgmt jdlx lmrkv fdcgjhm dmzrd dktgnm ggjk djlcbd lfrnc brkpckn fqfm lnd lpgg zshknhl dkjlhx pzns xhhp rqdggr kxjttzg qktlffz zfrg bhkrr bdnqhn ggzqx tnsmf nvnqk xvqxszc ldlpqdx rrqrbt flp qmmf qzbb trhm nbtvmr ssdp vpkrmfl jdtdbj hlqmb zzbvjz ndvrq zmmtvm fkjmz dlkpcfz ljkdmhpn kx gpskmh hbzlk ssk gfxdfvf mczhpbs dlmkn rclhlfv nqpds zjmdst gdg grqppvx hjsl dsvqv ldm sphnq qrbql rhzk bstzz mnzbc (contains shellfish, peanuts)
fqfm mnzbc kjkrm tnsmf jgkhfz lpgg rbrmc ggzqx xhhp xssj gjrlc rbrhg qmmf fkjmz hgmt zfhgv nnbsm rzhxzk bdnqhn jcsksnf sjmf fqlmnc vsp zpxcdt rk xcsdtgb hbzlk zctt nsjzj nvnqk gtgtrc dmthbf zmvhck gpskmh jdlx djxff sqbdlq lfrnc qcggn ggjhzzd zjmdst ttmfnxn lnt ldm kxgtgt jlszf rfgknb znkth rnmbgpv ndvrq fvqmjm cbslk xxkz (contains nuts, peanuts, sesame)
cgdjss rhq jgkhfz trhm rcp mnzbc shmpchr crtpbnp fkjmz qmkhfq qzvhx hjsl kjkrm chnnns zjmdst qzbb zfrg lnd xcsdtgb dktgnm dlkpcfz grqppvx krdxd jzfdv rk sjmf frskl vhgjx lhxr fqfm xhhp hrvcn zmmtvm sbpm rmrg hscj jdlx bstzz zgdllp flp rclhlfv fqlmnc dmthbf dmzrd rltdnr ckgd pzns ndvrq ldm cnkh lpgg vbtxrg djxff spqs nqmt ftzmnzv sqbdlq kxgtgt flkmb hscsj tjfp gpskmh vpkrmfl tvsj sphnq ftzd xnjn qctkc xvqxszc lpcjbk (contains shellfish)
fvqmjm rrqrbt lmrkv tjfp stlgtj zfhgv lscp gpskmh mmcff zzbvjz jdlx bfgktfm czjnmn jkttx rzhxzk rk jzfdv lksfxx xlqvs zfrg rvjpb zmmtvm kjkrm fqfm pzns zmvhck rbrmc hjsl vbtxrg bjksj ggjhzzd fkjmz brtrhg bxtkrc hrvcn kxgtgt zjmdst kxjttzg kxpv lgcdpd bhkrr djlcbd lhxr ndvrq fvdgnsr krdxd xgjl gtdvh zctt nnbsm vsp fhs mnzbc ljkdmhpn spqs gpqcmc nvnqk hqvn (contains eggs, sesame, peanuts)
jvhp mmrjb ggzqx zfrg rltdnr gpskmh zgdllp mmcff fkjmz dsvqv tjfp bfgktfm rrqrbt lpgg lpcjbk ldm jspbd qmmf sjcnnc lmrkv stlgtj xvqxszc cvts sqbdlq qktlffz dkh rk jhhp slhsqs ggjk xnjn fxmn vrsnfl fhs hgmt nvnqk zctt hscsj ssk mnzbc kjkrm zpxcdt kxpv jzfdv ggjhzzd vjjtq thlvnb rclhlfv xmm lksfxx zmmtvm ftzmnzv krdxd hqvn jlszf ndvrq fvdgnsr hnkbr spqs dtfj hql hrvcn brtrhg fqfm vpkrmfl lnt crd tvsj znkth kxjttzg bxtkrc flkmb jxfs (contains dairy, eggs)
xlqvs ndbq brkpckn crtpbnp ldlpqdx sphnq gpqcmc clkcq zzbvjz cvts jkttx bdnqhn frskl trhm xvqxszc ldm kjkrm gjrlc fqfm jcsksnf fvqmjm rbrmc jzfdv tjfp stsktc xxkz dmthbf bfgktfm zmmtvm tvsj nnbsm zctt mnzbc fhs qzvhx djlcbd fdgf qrz qktlffz ndvrq mczhpbs grqppvx ftzd fkjmz mfdrqvg jtm qmkhfq xgjl cnkh ftzmnzv krdxd kxpv rhpc bjsvt fqlmnc qrvq rmrg rclhlfv ssdp hql qmmf dsvqv jlck lpgg zgdllp kxjttzg rzhxzk (contains sesame, nuts, shellfish)
kxjttzg brkpckn kjkrm ljkdmhpn gtbhdgf rhq xssj cnkh zjmdst dmthbf kx gpskmh xlqvs xvqxszc tnsmf jgkhfz lfrnc pjsmxzmq ssdp bstzz fkjmz fvdgnsr rrqrbt ndvrq flp rhpc zgdllp crd gdg jdtdbj bfgktfm lpcjbk shmpchr fqfm qcggn ggjk cbslk fdgf ldm (contains sesame)
lksfxx xlqvs ckgd jdlx gjrlc mmrjb cgdjss zgdllp sqbdlq rnmbgpv czjnmn gdg mfdrqvg crd fdgf lhxr ldm dktgnm dmthbf ggzqx crtpbnp rqdggr znkth lnd tnsmf rcp vrsnfl hscj hlqmb zshknhl rvjpb mmcff kx zjmdst fqfm fkjmz bhkrr lpcjbk jdtdbj mnzbc dsvqv pzns ndvrq rzhxzk brkpckn kxjttzg tvsj flp dlkpcfz xxkz dkjlhx hql (contains dairy)
lfrnc nzcz kxgtgt rmrg dxd cnkh qrvq zzbvjz fqfm rrqrbt zctt xnjn flp nsjzj fdgf sjcnnc gtgtrc dsvqv kx crd lkzkq cbslk lgcdpd kjkrm lmrkv jzfdv ttmfnxn grqppvx mmcff ldm jlck rzhxzk lnd rclhlfv hscj lpcjbk kxjttzg sbpm mnzbc xcsdtgb stsktc qctkc chnnns krdxd dmzrd lscp trhm rk dlkpcfz ndvrq xmm gpqcmc kxpv ptzxb bjsvt zjmdst sdgttdh rqdggr (contains fish)
krdxd fkjmz fqfm hql kx hqvn lkzkq jcsksnf ttmfnxn xssj rzhxzk vsp hjsl xvqxszc nqpds kjkrm bxtkrc grqppvx qmkhfq rltdnr rnmbgpv lfrnc dxd kxjttzg djlcbd gtgtrc cgdjss cnkh lscp xlqvs rbrmc brkpckn znkth mmrjb ldm glpjxr zjmdst vrsnfl ndvrq hlqmb zmmtvm slhsqs ggzqx mkjjr npn rk dkjlhx frskl (contains eggs)
kx hjsl flkmb rzhxzk mnzbc kjkrm mczhpbs gpqcmc bfgktfm rdgp fdcgjhm rnmbgpv lksfxx sjcnnc grqppvx zfrg vsp ckgd jdtdbj qmmf qrvq zjmdst lpgg jdlx frskl lsfktq sphnq qktlffz bstzz ldm rhq tvsj qmkhfq crtpbnp kxjttzg dlmkn ndbq qzvhx glpjxr stsktc fqfm dkjlhx pjsmxzmq rmrg zjzjcx qzbb xnjn hrvcn tgtkk nsjzj nqmt czjnmn ljkdmhpn tnsmf kxpv bjksj nnbsm rhzk rhpc lfrnc lkzkq qkmst dsvqv bdnqhn jlszf fkjmz (contains fish, dairy, eggs)
gtgtrc brkpckn qmkhfq sdgttdh glpjxr ssdp fkjmz vsp zjzjcx rhzk hgmt crd jdtdbj qktlffz kjkrm sqbdlq chnnns rmrg bjsvt gjrlc ldm tgtkk zjmdst jvhp hql ckgd thlvnb jkttx tvsj bstzz gpskmh mmcff dmzrd kxjttzg nnbsm cgdjss qctkc nsjzj kxgtgt nzcz qcggn fxmn ggjk znkth dkjlhx zhxhfm dmthbf rbrhg mkjjr jhhp clkcq jgkhfz slhsqs zgdllp mnzbc rvjpb bdnqhn qmmf zfrg hnkbr ftzmnzv dktgnm qrbql zctt jrk vjjtq fqfm (contains peanuts, nuts)
tjfp lnd ldm ndvrq thlvnb xmm rhzk rzmb hjsl nvnqk hbzlk rbrmc hqvn tnsmf ggjhzzd jcsksnf jrk lgcdpd dkjlhx glpjxr mnzbc trhm slhsqs nnbsm sjmf kjkrm qkmst rhpc xcsdtgb crtpbnp jzfdv nqmt xssj gtbhdgf ljkdmhpn xnjn qktlffz kx zjmdst sdgttdh lhxr qctkc zfhgv bfgktfm zfrg rhq sqbdlq ldlpqdx krdxd jvhp lnt bjsvt gtgtrc lmrkv mmrjb hrvcn xvqxszc vjjtq mmcff fqfm bjksj flkmb bstzz kxjttzg dxd zpxcdt clkcq crd dtfj mczhpbs rvjpb jgkhfz dlmkn (contains fish, eggs)
ckgd hqvn flkmb hrvcn zgdllp ftzmnzv zzbvjz dlmkn lnt rzhxzk vsp rk brkpckn sdgttdh hql nsjzj fdgf xnjn lscp kxpv kxjttzg chnnns jspbd xmm rltdnr fkjmz rclhlfv mnzbc ndvrq krdxd bstzz hjsl qrvq rhpc gfxdfvf hlqmb rqdggr jxfs gtgtrc ftzd nvnqk rcp jdlx thlvnb vpkrmfl ljkdmhpn fqfm clkcq lkzkq ldlpqdx gtbhdgf glpjxr shmpchr dlkpcfz jtm mkjjr zmvhck ttmfnxn bjqzq zjmdst bdnqhn bhkrr ldm xgjl (contains nuts, fish, dairy)
vpkrmfl ggzqx lkzkq nsjzj lsfktq flp lpcjbk zgdllp djxff qzbb ldlpqdx cbslk kjkrm rzmb ptzxb zjmdst ldm ttmfnxn djlcbd kxjttzg mnzbc brkpckn grqppvx rnmbgpv rzhxzk mmrjb nzcz nvnqk hqvn hlqmb xnjn rcp jkttx gpskmh vhgjx xhhp hgmt dxd ssk fqfm xxkz hrvcn trhm spqs tgtkk bstzz qmmf jlck dmzrd dsvqv qrz fvqmjm rrqrbt dkjlhx qctkc ndvrq jrk ssdp (contains dairy, wheat, fish)
fxmn kx lfrnc qrvq rhq bdnqhn pjsmxzmq kxgtgt zctt qzbb ndvrq rnmbgpv fqfm zgdllp xxkz pzns rdgp lpgg zjmdst tnsmf trhm hjsl shmpchr rltdnr jtm bjsvt xvqxszc mnzbc fdcgjhm flp rmrg lksfxx gpqcmc ptzxb vhgjx zfhgv bfgktfm qrz jgkhfz rbrmc gtdvh hnkbr jvhp dxd ldm rcp ttmfnxn hscsj kxjttzg ggjhzzd jrk mczhpbs sjmf zhxhfm fkjmz zzbvjz nsjzj mmrjb jkttx lgcdpd (contains dairy, fish, peanuts)
ldm dkh zhxhfm zmmtvm znkth bhkrr xcsdtgb dmzrd cbslk gjrlc lnd hjsl ggzqx bdnqhn xmm bfgktfm zfrg ndvrq crd ftzd hqvn cvts qctkc fvqmjm rhpc slhsqs tnsmf dkjlhx stsktc tgtkk hscsj xlqvs nbtvmr fvdgnsr jspbd lgcdpd dtfj zzbvjz cgdjss lscp rmrg crtpbnp djxff xhhp ndbq zfhgv bjqzq rltdnr fqfm rbrhg jgkhfz krdxd dmthbf gtbhdgf fkjmz rvjpb kxjttzg frskl glpjxr jlszf fdgf lmrkv qktlffz sjmf xvqxszc dlkpcfz fhs qzvhx mfdrqvg lksfxx kxgtgt ttmfnxn mmrjb tjfp sdgttdh zjmdst jtm sbpm mnzbc dxd rcp ggjk xnjn rclhlfv nqpds (contains sesame, fish)
jspbd fdgf bjsvt nqpds ndbq lkzkq cnkh trhm rnmbgpv mmrjb zctt gtgtrc nvnqk sjcnnc gdg nqmt xvqxszc dmzrd lpgg rhzk nnbsm fqfm xlqvs rk rzmb fvqmjm bxtkrc zmmtvm hlqmb jvhp rhq vbtxrg hscsj slhsqs zjmdst ndvrq ftzd jzfdv mfdrqvg vjjtq dmthbf brkpckn xmm cvts bstzz jdtdbj sqbdlq bfgktfm ldm hql rbrmc fkjmz jrk fxmn ftzmnzv npn kxjttzg rcp kjkrm kxgtgt xssj qzvhx dlkpcfz ssk (contains shellfish)
gdg qkmst zjmdst xgjl ptzxb xnjn jrk gpskmh jkttx trhm nqpds qmmf lnd jdtdbj krdxd lkzkq fqlmnc qmkhfq lpcjbk ndvrq czjnmn znkth xxkz ssk zfhgv rqdggr vbtxrg djxff kxjttzg hql fqfm tjfp xcsdtgb kjkrm zhxhfm mkjjr thlvnb ckgd jspbd pjsmxzmq chnnns ggjhzzd nqmt djlcbd sdgttdh vrsnfl qzbb mnzbc frskl qrbql nnbsm jlck zzbvjz gtgtrc cbslk fkjmz hscsj bhkrr flkmb rzmb lksfxx (contains dairy)
zfrg vjjtq rk lnt fqfm dlkpcfz lpgg sdgttdh grqppvx bhkrr kx dsvqv ftzd ckgd crtpbnp vbtxrg ljkdmhpn gtgtrc thlvnb nzcz jrk zjmdst fkjmz zctt ndvrq ggjhzzd mnzbc qrz gjrlc ldlpqdx jdtdbj bjqzq fdcgjhm rdgp tnsmf kjkrm ssk rltdnr nqmt dmthbf tjfp djlcbd bxtkrc hql mmrjb qcggn krdxd cgdjss kxjttzg zgdllp sjmf zmmtvm lpcjbk lmrkv qkmst bjsvt (contains eggs, wheat, nuts)
lhxr dlkpcfz lmrkv zshknhl hjsl gpqcmc fdcgjhm zjmdst jdtdbj jkttx qzvhx xlqvs rvjpb vpkrmfl nqpds hlqmb glpjxr crd rmrg kjkrm lgcdpd rclhlfv rdgp gtbhdgf zpxcdt rhq gjrlc ldm grqppvx bjqzq kxgtgt nbtvmr dktgnm kxjttzg zmvhck rhpc rcp fvqmjm zhxhfm jcsksnf chnnns lscp gfxdfvf mnzbc xhhp dmthbf fqlmnc ftzmnzv lksfxx qmkhfq ndvrq fdgf jgkhfz czjnmn npn cgdjss sdgttdh fkjmz (contains shellfish, sesame, nuts)
bhkrr lnt vpkrmfl nnbsm gfxdfvf xxkz crtpbnp rhzk mkjjr flkmb sqbdlq jxfs jhhp npn zshknhl fqlmnc cgdjss bxtkrc hgmt hscsj rvjpb czjnmn qktlffz qcggn znkth zfrg lgcdpd nvnqk cnkh rbrmc xssj gtbhdgf fdgf xvqxszc tvsj ckgd hlqmb dtfj grqppvx pjsmxzmq tjfp gpskmh hrvcn kxpv sphnq rk lmrkv dktgnm bjqzq mfdrqvg zjmdst kxjttzg ndvrq zfhgv qrbql djlcbd fqfm mnzbc bfgktfm kjkrm jzfdv tnsmf fkjmz brtrhg jkttx mczhpbs gpqcmc ssdp qctkc brkpckn (contains peanuts, sesame)
zctt dtfj hnkbr jzfdv vbtxrg chnnns sqbdlq rbrmc kjkrm clkcq hgmt mmrjb lnt mczhpbs brtrhg bjqzq mnzbc slhsqs ndvrq thlvnb fqlmnc rmrg zhxhfm cbslk bstzz zjmdst fqfm mmcff kxjttzg crtpbnp tgtkk shmpchr lhxr ggjk cnkh xlqvs sphnq vhgjx gtbhdgf qctkc ldm sbpm znkth zzbvjz jdtdbj ptzxb cgdjss zfhgv vrsnfl dmzrd jcsksnf hlqmb (contains eggs)
lnt ftzmnzv djlcbd gtgtrc rhq lsfktq dkjlhx dmthbf pjsmxzmq zfrg jzfdv xvqxszc sphnq cgdjss clkcq ndbq nnbsm hqvn jcsksnf zjmdst rnmbgpv vsp jspbd zmvhck nqmt ndvrq sbpm bxtkrc grqppvx lhxr dsvqv jkttx fvqmjm bdnqhn mmrjb jtm rhzk lfrnc dtfj mfdrqvg fqfm kxjttzg fkjmz xmm gfxdfvf dxd ggjhzzd nsjzj zgdllp mnzbc vbtxrg xnjn brkpckn vpkrmfl lpcjbk lgcdpd zshknhl kjkrm rbrhg hjsl tgtkk vjjtq mmcff zjzjcx qmmf ptzxb qcggn dkh qkmst rk bstzz kx qrvq rrqrbt rmrg bjksj lksfxx sjmf hscj frskl ckgd krdxd ftzd sqbdlq tvsj rvjpb fvdgnsr crd dktgnm npn qzbb qrz (contains wheat, shellfish, nuts)"""


lines = inp.split("\n")

from collections import defaultdict
ingredients = defaultdict(list)
allergens = defaultdict(list)

ing_cnt = defaultdict(int)
all_cnt = defaultdict(int)

for line in lines:
    ing, al = line.split(" (contains ")
    for a in al[:-1].split(", "):
        all_cnt[a] = all_cnt[a] + 1
    for i in ing.split(" "):
        ing_cnt[i] = ing_cnt[i] + 1
        for a in al[:-1].split(", "):
            ingredients[i].append(a)
            allergens[a].append(i)

# print(ingredients)
# print(allergens)
cdil = []
while(True):
    allc = defaultdict(list)
    for k,v in allergens.items():
        allc[k] = v[:]
    for al in allc:
        cnt = defaultdict(int)
        for ing in allergens[al]:
            cnt[ing] = cnt[ing] + 1
        poss = []
        for ing in cnt:
            if cnt[ing] == all_cnt[al]:
                poss.append(ing)

        # print(al, cnt)
        if len(poss) == 1:
            for all in allergens:
                allergens[all] = list(filter(lambda i: i != poss[0], allergens[all]))
            cdil.append((poss[0], al))
        #if len(allc[al]) == 1:
        #    for all in allergens:
        #        allergens[all] = list(filter(lambda i: i != allc[al][0], allergens[all]))
            
    # print(allergens)
    if allc == allergens:
        break
sol = 0
# print(ing_cnt)
tings = set()
# print(allergens)
for a in allergens:
    for i in allergens[a]:
        tings.add(i)
for i in tings:
    sol += ing_cnt[i]

for i, a in sorted(cdil, key = lambda ia : ia[1]):
    print(i, end=",")
print()
print(sol)