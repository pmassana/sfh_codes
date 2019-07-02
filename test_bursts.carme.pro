

; t = mrdfits('madre_z0001_z03q04b05.HRD_GOOD.dis_new2_no99.fits.gz',1)

k = lindgen(1e2)

ageb = [0., 0.5, 1., 1.5, 2., 2.5, 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14.]
metb = [0.0004, 0.0007, 0.0011, 0.0016, 0.0022, 0.0029, 0.0037, 0.0046, 0.0056, 0.0067, 0.0079, 0.0092, 0.0106, 0.0122, 0.0140, 0.0160, 0.0182, 0.0206, 0.0232, 0.0260, 0.0290]


age = t.age/1e9
met = t.metal

b1 = where(age gt 0.0 and age le 0.5 and met gt 0.0160 and met le 0.0182, n1)
b2 = where(age gt 1.0 and age le 1.5 and met gt 0.0140 and met le 0.0160, n2)
b3 = where(age gt 2.5 and age le 3.0 and met gt 0.0122 and met le 0.0140, n3)
b4 = where(age gt 6.0 and age le 7.0 and met gt 0.0079 and met le 0.0092, n4)
b5 = where(age gt 10. and age le 11. and met gt 0.0037 and met le 0.0046, n5)
b6 = where(age gt 13. and age le 14. and met gt 0.0007 and met le 0.0011, n6)

b = [b1, b2, b3, b4, b5, b6]


window, 0
plot,t[k].age/1e9,t[k].metal,psym=3,/xsty

oplot,t[b].age/1e9,t[b].metal,psym=3

for j=0, n_elements(metb)-1 do $
    oplot,[ageb[0],ageb[-1]],[metb[j],metb[j]],col=cgcolor("red"),thi=3

for j=0, n_elements(ageb)-1 do $
    oplot,[ageb[j],ageb[j]],[metb[0],metb[-1]],col=cgcolor("red"),thi=3



window, 1
plot,t[k].g-t[k].i,t[k].i,psym=3,yr=[7,-5],/ysty,xr=[-1,3]
oplot,t[b].g-t[b].i,t[b].i,psym=3,col=cgcolor("blue")



; nam = ['id','x','y','g','gerr','i','ierr','age','metal']
; ; ty = ['I', 'I', 'I', 'F', 'B', 'F', 'B', 'F', 'I', 'F', 'F']
; ty = ['B', 'B', 'B', 'D', 'B', 'D', 'B', 'F', 'F']
; create_struct, fld, '', nam, ty
; fld = replicate(fld, n_elements(b))
; 
; fld.g     = t[b].g
; fld.i     = t[b].i
; fld.age   = t[b].age
; fld.metal = t[b].metal
; 
; mwrfits, fld, '6bursts.fits',/create


;;; normalization:
metran = 0.03-0.0001

ra = [[0.0160, 0.0182], $
      [0.0140, 0.0160], $
      [0.0122, 0.0140], $
      [0.0079, 0.0092], $
      [0.0037, 0.0046], $
      [0.0007, 0.0011]]

norm = transpose((ra[1,*]-ra[0,*])/metran)

fact = 0.01/norm * [n1, n2, n3, n4, n5, n6]
; print, fact

bcst = [b1[0:fact[0]-1], b2[0:fact[1]-1], b3[0:fact[2]-1], b4[0:fact[3]-1], b5[0:fact[4]-1], b6[0:fact[5]-1]]   ;;; same ampl. for all bursts


;;; SFR corresponding to selection:
window, 2
plot,[0,0,0.5,0.5,1,1,1.5,1.5,2.5,2.5,3.,3.,6.,6.,7.,7.,10.,10.,11.,11.,13.,13.,14.,14.],[0,norm[0],norm[0],0,0,norm[1],norm[1],0,0,norm[2],norm[2],0,0,norm[3],norm[3],0,0,norm[4],norm[4],0,0,norm[5],norm[5],0]  ;;; before normalization

oplot,[0,0,0.5,0.5,1,1,1.5,1.5,2.5,2.5,3.,3.,6.,6.,7.,7.,10.,10.,11.,11.,13.,13.,14.,14.],[0,0.01,0.01,0,0,0.01,0.01,0,0,0.01,0.01,0,0,0.01,0.01,0,0,0.01,0.01,0,0,0.01,0.01,0],line=2  ;;; after normalization


; nam = ['id','x','y','g','gerr','i','ierr','age','metal']
; ; ty = ['I', 'I', 'I', 'F', 'B', 'F', 'B', 'F', 'I', 'F', 'F']
; ty = ['B', 'B', 'B', 'D', 'B', 'D', 'B', 'F', 'F']
; create_struct, fld, '', nam, ty
; fld = replicate(fld, n_elements(bcst))
; 
; fld.g     = t[bcst].g
; fld.i     = t[bcst].i
; fld.age   = t[bcst].age
; fld.metal = t[bcst].metal
; 
; mwrfits, fld, '6bursts_sameampl.fits',/create



bun1 = [[ 0.00, -0.60, -0.70,  0.45,  0.90, 0.0],[ 4.50,  3.10,  1.50,  1.50,  4.50, 4.50]]
bun2 = [[ -0.70, -0.85, -0.60,  0.45, -0.70],[ 1.50, -3.00, -3.00,  1.50,  1.50]]
bun3 = [[ 0.60,  0.60,  1.25,  1.10,  0.83],[ 2.40,  1.50,  1.50,  4.00,  4.00]]

wset, 1
; plot,t[k].g-t[k].i,t[k].i,psym=3,yr=[6,-4],/ysty,xr=[-1,2]

oplot,bun1[*,0],bun1[*,1],thi=3;,col=cgcolor("blue")
oplot,bun2[*,0],bun2[*,1],thi=3;,col=cgcolor("blue")
oplot,bun3[*,0],bun3[*,1],thi=3;,col=cgcolor("blue")




end
